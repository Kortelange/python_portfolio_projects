from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    
    # Configuration settings can go here
    app.config['SECRET_KEY'] = 'your_secret_key'
    from .routes import main

    app.register_blueprint(main)
    
    return app
