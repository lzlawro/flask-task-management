import os

class Config:
    # 独立出配置硬代码，可以适应不同操作系统
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'inspur-pre-entry-secret-key' # 加密功能占位符