from flask import Flask, session


def create_app():
    app = Flask(__name__)
    
    # Configuration settings can go here
    app.config['SECRET_KEY'] = 'your_secret_key'
    from .routes import main, morse_code, tic_tac_toe

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(morse_code, url_prefix="/morse_code")
    app.register_blueprint(tic_tac_toe, url_prefix="/tictactoe")
    
    return app
