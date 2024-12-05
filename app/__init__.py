# app/__init__.py

from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    from app.routes.data_routes import bp as data_bp
    app.register_blueprint(data_bp)

    # Ensure the instance folder exists
    try:
        import os
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Test route
    @app.route('/test/')
    def test_page():
        return 'Hello from Flask!'

    return app