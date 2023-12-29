# blueprint/routes/__init__.py
from flask import Flask
from flask_cors import CORS
from models.models import db
from blueprint.routes.user import bp_user
from blueprint.routes.commodity import bp_commodity


def create_app():
    app = Flask(__name__)
    CORS(app)
    # app.config.from_pyfile('config.py')
    app.config.from_pyfile('D:\\package\\code\\flask_ei\\config.py')

    db.init_app(app)
    register_blueprint(app)

    return app

    # 注册蓝图


def register_blueprint(app: Flask):
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_commodity)
