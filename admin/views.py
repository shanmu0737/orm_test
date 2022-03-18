import datetime
from flask import render_template,redirect,url_for,request
from flask.views import MethodView
from personal.models import *
from personal.froms import EmployeeForm

from admin import admin

# @admin.route('/emp/list')
# def emp_list():
#     items = db.session.query(Employee).limit(10)     #显示前10条数据
#     return render_template('admin/bank-table.html',items=items)

#基于类的视图，查看员工记录
class EmployeeListView(MethodView):
    def get(self,page=1):
        items = Employee.query.paginate(page, per_page=10)  #paginate第一个值：第几页，第二个值显示几条
        return render_template('admin/bank-table.html',employees=items)

#删除一个员工操控
class EmployeeDelView(MethodView):
    def get(self,id=None):
        if id:
            emp = db.session.query(Employee).get(id)        #get只适合传递主键
            if emp:
                db.session.delete(emp)
                db.session.commit()
        return redirect(url_for('.emp_list'))

#添加用户表单
# class EmployeeCreatView(MethodView):
#     def get(self):
#         departments = db.session.query(Department).all()
#         return render_template('admin/emp-detail.html',departments=departments)
#
#     def post(self):
#         employee = Employee(
#             request.form.get('name'),
#             request.form.get('gender', '男'),
#             request.form.get('job'),
#             datetime.strptime(request.form.get('birthdate'),'%Y-%m-%d'),
#             request.form.get('idcard'),
#             request.form.get('address'),
#             float(request.form.get('salary'))
#         )
#         employee.depaitment_id = request.form.get('depaitment_id')
#
#         db.session.add(employee)
#         db.session.commit()
#         return redirect(url_for('.emp_list'))

class EmployeeCreatOrEdit(MethodView):
    def get(self, id=None):
        #如果id为空，则为添加操作
        #否则为编辑制作
        emp = Employee() if not id else db.session.query(Employee).get(id) #三元表达式
        # emp = Employee()    #创建一个员工类实例
        # if id:              #如果id有值的话，查看id,如果id没有值，则合建Empoyee()
        #     emp = db.session.query(Employee).get(id)    #查询id
        # 给form两个值，如果第一个找不到，则找第二个
        form = EmployeeForm(request.form, obj=emp)
        #获取部门Department.query.all()
        # form.department_id.choices = [(d.id, d.name) for d in Department.query.all()]
        form.depaitment_id.choices = [(d.id, d.name) for d in Department.query.all()]
        form.gender.choices = [('男','男'),('女','女')]
        return render_template('admin/emp-edit.html',form=form)

    def post(self, id=None):
        #如果表单提交数据包括id,测为编辑，否则为添加
        form = EmployeeForm(request.form) #导入所有form的值
        #如果是添加的话，建个新的Employee，如果是修改的话，去数据库把内容抠出来
        emp = Employee(
            # form.name.data,
            # form.gender.data,
            # form.job.data,
            # form.birthdate.data,
            # form.idcard.data,
            # form.address.data,
            # form.salary.data,

            # None,
            # None,
            # None,
            # None,
            # None,
            # None,
            # None,
            # datetime.now()
        ) if not id else db.session.query(Employee).get(id)
        form.populate_obj(emp)
        #如果没有id,添加emp; 如果有id,是编辑不用处理
        if not id:
            db.session.add(emp)
        db.session.commit()
        return redirect(url_for('.emp_list'))

