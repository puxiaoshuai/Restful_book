from flask import Flask
from app.api_1_0 import bp_book
from exts import db
import config

def create_app():
    app = Flask(__name__)
    # 绑定配置文件
    app.config.from_object(config)
    # 注册蓝图
    app.register_blueprint(bp_book)
    db.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
