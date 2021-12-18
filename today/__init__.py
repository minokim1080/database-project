from flask import Flask, request, render_template, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


naming_convention = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%)column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
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
    from .views import main_views, auth_views, cloth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(cloth_views.bp)

    return app
