from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///./db/myblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True        #执行时显示sql语句

db = SQLAlchemy(app)

#生成数据库
@app.route('/db/')
def intialize():
    db.create_all()
    return 'ok'

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
