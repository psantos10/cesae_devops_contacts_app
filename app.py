from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.development.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@cesae_contacts_app_postgres:5432/cesae_contacts_app'

    db.init_app(app)

    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    return app
