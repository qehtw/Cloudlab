# Deploying Cloudlab REST service to AWS (ECR + ECS Fargate) with autoscaling

This document contains steps and helper scripts added to this repository to:

- Build a Docker image for the Flask REST service (Dockerfile added)
- Push the image to Amazon ECR (PowerShell script provided)
- Deploy an ECS Fargate service fronted by an ALB with Application Auto Scaling (CloudFormation template)
- Run a simple load generator against the service to exercise autoscaling (async Python script)

Files added
- `Dockerfile` — container image for the app (gunicorn served on port 8000).
- `scripts/build_push_ecr.ps1` — PowerShell helper to build and push an image to ECR.
- `cloudformation/ecs_fargate_autoscaling.yaml` — CloudFormation template to create ECS resources and autoscaling (parameterized).
- `tools/load_test.py` — Async load generator using `aiohttp`.
- `README_AWS_CONTAINER.md` — this file with step-by-step instructions.

Prerequisites
- AWS CLI v2 configured (or specify `--profile` when running the PS script).
- Docker installed and running locally (for image build/push).
- Python 3.8+ for the load generator and `pip install aiohttp`.

1) Build & push image to ECR

Create an ECR repository (example):

```powershell
aws ecr create-repository --repository-name cloudlab --region us-east-1
```

Take note of the repository URI returned (e.g. 123456789012.dkr.ecr.us-east-1.amazonaws.com/cloudlab).

Build and push using the included PowerShell script (from repo root):

```powershell
.
\scripts\build_push_ecr.ps1 -EcrUri 123456789012.dkr.ecr.us-east-1.amazonaws.com/cloudlab -ImageTag v1 -Region us-east-1 -Profile default
```

This will: docker login to ECR, build the image and push the tag.

2) Prepare network info (use your default VPC/subnets or your own)

Get the default VPC id:

```powershell
$vpc = aws ec2 describe-vpcs --filters "Name=isDefault,Values=true" --query "Vpcs[0].VpcId" --output text
Write-Host "Default VPC: $vpc"
```

Get subnets in that VPC (pick 2+ subnets for ALB):

```powershell
aws ec2 describe-subnets --filters "Name=vpc-id,Values=$vpc" --query 'Subnets[].SubnetId' --output text
```

Create (or reuse) a Security Group that allows inbound HTTP (port 80) from 0.0.0.0/0 and outbound to anywhere. Note its id (e.g. sg-...).

3) Deploy the CloudFormation stack (ECS + ALB + autoscaling)

Use the template `cloudformation/ecs_fargate_autoscaling.yaml`. When deploying, pass your VPC/Subnets/SecurityGroup and the pushed ImageUri.

Example (PowerShell):

```powershell
$imageUri = "123456789012.dkr.ecr.us-east-1.amazonaws.com/cloudlab:v1"
$subnets = "subnet-123 subnet-456"  # space-separated list; CF expects List<Subnet::Id>
$sg = "sg-0123456789abcdef0"

aws cloudformation deploy --stack-name cloudlab-ecs --template-file cloudformation/ecs_fargate_autoscaling.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides ImageUri=$imageUri VpcId=$vpc SubnetIds="$subnets" SecurityGroupIds="$sg" DesiredCount=1 MinCapacity=1 MaxCapacity=4 TargetCPUUtilization=50
```

When the stack finishes, the output `LoadBalancerDNS` will contain the ALB DNS name you can use to call the service.

4) Run the load generator to exercise autoscaling

Install the load-generator dependency and run the simple tool:

```powershell
python -m pip install aiohttp
python tools\load_test.py --url http://<ALB_DNS>/ --concurrency 50 --duration 300
```

Tune `--concurrency` and `--duration` to increase load. The script prints periodic stats and a final report.

5) Observe autoscaling and metrics

- ECS Console > Clusters > (your cluster) > Services will show the desired and running tasks. The Events tab shows scale in/out and deployment events.
- CloudWatch > Metrics > ECS or ALB TargetGroup to track CPUUtilization, RequestCount, and target health.
- CloudWatch Logs > /aws/ecs/cloudlab (or the log group created by the template) to inspect container logs.

Notes, limitations and next steps

- The CloudFormation template requires you to provide VPC/Subnet/SecurityGroup parameters. This is intentional to avoid creating new VPCs in your account.
- The template configures CPU-based target tracking. You can add a memory-based policy or custom CloudWatch alarms if you prefer.
- For production, consider using HTTPS on the ALB, private subnets for tasks, and more fine-grained IAM.
- If you'd like, I can add a Terraform version, or a GitHub Actions workflow to build/push automatically and trigger deployment.
