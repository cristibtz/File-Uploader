from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .config import BaseConfig
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(BaseConfig)

    db.init_app(app)

    app.config['UPLOAD_FOLDER'] = os.getcwd() + "/uploads"
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .routes import upload, download

    app.register_blueprint(upload, url_prefix="/")
    app.register_blueprint(download, url_prefix="/download")

    from .models import Files

    return app

