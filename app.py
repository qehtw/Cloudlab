from app import create_app
from flasgger import Swagger

app = create_app()

# Підключаємо Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # Підключаємо всі роутінги
            "model_filter": lambda tag: True,  # Підключаємо всі моделі
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs"  # Ось посилання для UI
}
swagger = Swagger(app, config=swagger_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
