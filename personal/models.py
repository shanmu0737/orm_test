from datetime import datetime
from pms_18_class import db

class Department(db.Model):
    """部门"""
    __tablename__ = 'department'

    id = db.Column(db.Integer,primary_key=True)     #主键
    name = db.Column(db.String, unique=True)        #是否唯一

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<部门{} : {} >'.format(self.id,self.name)

class Employee(db.Model):
    """员工表"""
    __tablename__ = 'employee'
    id = db.Column(db.Integer,primary_key=True)     #主键
    name = db.Column(db.String(50))
    gender = db.Column(db.String)
    job = db.Column(db.String)
    birthdate = db.Column(db.DateTime)
    idcard = db.Column(db.String)
    address = db.Column(db.String)
    salary = db.Column(db.Float)    #浮点型
    release_time = db.Column(db.DateTime)


    def __init__(self,name=None,gender=None,job=None,birthdate=None,idcard=None,
                 address=None,salary=0.00,release_time=None):
        self.name = name
        self.gender = gender
        self.job = job
        self.birthdate = birthdate
        self.idcard = idcard
        self.address = address
        self.salary = salary
        self.release_time = release_time if release_time else datetime.now()

    #表现部门表和员工表之间的关联,#外键，department表名，id
    depaitment_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    #类成员关系,Department是类名,backref是指反向引用,employees不是表名，是何意名，lazy是延迟查询
    depaitment = db.relationship('Department',backref=db.backref('employees',lazy='dynamic'))

    def __repr__(self):
        return '<员工 {}：{} {} {}>'.format(self.id,self.name,self.salary,self.address)



















