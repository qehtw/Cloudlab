Param(
    [Parameter(Mandatory=$true)]
    [string]$EcrUri,

    [string]$ImageTag = "latest",

    [string]$Region = "us-east-1",

    [string]$Profile
)

if ($Profile) {
    Write-Host "Using AWS CLI profile: $Profile"
    $env:AWS_PROFILE = $Profile
}

Write-Host "Logging into ECR: $EcrUri (region $Region)"
$login = aws ecr get-login-password --region $Region 2>&1
if ($LASTEXITCODE -ne 0) { throw "Failed to get ECR login password: $login" }

$login | docker login --username AWS --password-stdin $EcrUri
if ($LASTEXITCODE -ne 0) { throw "Docker login to ECR failed" }

$fullTag = "$EcrUri:$ImageTag"
Write-Host "Building image $fullTag"
docker build -t $fullTag .
if ($LASTEXITCODE -ne 0) { throw "Docker build failed" }

Write-Host "Pushing image $fullTag"
docker push $fullTag
if ($LASTEXITCODE -ne 0) { throw "Docker push failed" }

Write-Host "Image pushed: $fullTag"
