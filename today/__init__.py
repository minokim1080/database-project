from flask import Flask, request, render_template, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    #블루프린트
    from .views import main_views,login_views, auth_views, select_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(login_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(select_views.bp)

    return app
