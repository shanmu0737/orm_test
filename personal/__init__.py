from flask import Blueprint

#当有文件导入personal文件的时候，init文件先运行

#重要，顺序1，先创建蓝图
employee = Blueprint('employee',__name__)
#重要，顺序2，导入views
from personal.views import *