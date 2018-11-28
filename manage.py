from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from app_book import create_app

app = create_app()
manage = Manager(app=app)
Migrate(app=app, db=db)
# 增加db命令
# 比如在控制台执行  python manage.py db   [init,migrate,upgrade]
manage.add_command('db', MigrateCommand)









# 增加参数  @manage.option('-u', '--username', dest='username')
#   增加测试函数 @manage.command
#     def create_role():
