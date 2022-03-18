from flask import Blueprint,render_template
from flask.views import MethodView
from pms_18_class import db
from personal import employee       #从personal文件__init__中导入employee
from .models import Employee,Department         #同级目录导入

#查询员工表0到10页
class EmployeeListView(MethodView):
    def get(self):
        employees = db.session.query(Employee).all()[:10]
        return render_template('admin/bank-table.html',employees=employees)
        # return str(employees)

#访问地址
employee.add_url_rule('/list/',view_func=EmployeeListView.as_view('emp_list'))














