from flask import Flask

from wtforms import StringField
from app.web import web


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    # 注册蓝图
    app.register_blueprint(web)
    return app