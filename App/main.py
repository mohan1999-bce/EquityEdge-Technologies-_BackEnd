from flask import Flask
from flask_cors import CORS
from App.config import Config
from App.extensions import db
from App.Routes.user_routes import user_bp
from App.Routes.portfolio_routes import portfolio_bp
from App.Routes.investment_routes import investment_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
    app.register_blueprint(investment_bp, url_prefix='/investment')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


