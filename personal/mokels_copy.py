from flask import Flask
from pms_18_class import db
from datetime import datetime

class Banji(db.Model):
    """表名：班级"""
    __tablename__ = 'banji'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,unique=True)

    def __init__(self):
        self.name

    def __repr__(self):
        return '部门{}:{}'.format(self.id,self.name)

class Student(db.Model):
    """学生表"""
    __tablename__ = 'student'

    id = db.Column(db.Integer,primary_key=True) #主键
    name = db.Column(db.String(50))
    gender = db.Column(db.String)
    score = db.Column(db.String)
    telephone = db.Column(db.String)
    admission_time = db.Column(db.DateTime)

    def __init__(self,name,gender,score,telephone,admission_time=None):
        self.name = name
        self.gender = gender
        self.score = score
        self.telephone = telephone
        self.admission_time = admission_time if admission_time else datetime.now()

    #关联外键
    banji_id = db.Column(db.Integer,db.ForeignKey('banji.id'))
    student = db.relationship('Banji',backref=db.backref('students',lazy='dynamic'))

    def __repr__(self):
        return '<学生{}：{} {} {}>'.format(self.id, self.score, self.telephone)


