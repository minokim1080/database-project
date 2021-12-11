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
    with app.app_context():
        if db.engine.url.drivername == 'sqlite':
            migrate.init_app(app, db, render_as_batch=True)
        else:    
            migrate.init_app(app, db, compare_type=True)
    from . import models

    #블루프린트
    from .views import main_views,login_views, auth_views, select_views, result_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(login_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(select_views.bp)
    app.register_blueprint(result_views.bp)

    return app
