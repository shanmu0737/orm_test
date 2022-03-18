from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from admin import admin as blueprint_admin      #as后面是别名

app = Flask(__name__,static_url_path='')
app.secret_key = 'fkldjsfREIOR343453dj'
app.debug = True

#数据库连接信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/personal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True    #执行时，把sql语句显示出来

#关联上下文
db = SQLAlchemy(app)

# #导入views内容
# from personal.views import employee
# #蓝图规则 /emp为前缀
# app.register_blueprint(employee, url_prifix="/emp")


@app.route('/')
def index():
    return render_template('admin/bank-table.html')

from personal import employee

# 注册一个蓝图
app.register_blueprint(employee,url_prefix='/emp')

@app.route('/reg/',methods=['GET','POST'])
def user_reg():
    from validation.forms import UserRegForm
    form = UserRegForm(request.form)
    if request.method == 'POST' and form.validate():    #validate作用是所有数据都通过
    # if form.validate_on_submit():   #作用同上，为数据提交了并且验证通过
        return str(form.data)
    return render_template('user-reg.html',form=form)


@app.route('/test/')
def test():
    # return render_template('admin/test.html')
    return render_template('admin/emp-detail.html')
#注册一个蓝图
app.register_blueprint(blueprint_admin,url_prefix='/admin')

if __name__ == '__main__':
    app.run()