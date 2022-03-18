from flask import Blueprint

admin = Blueprint('admin',__name__)

from admin.views import *

#注册一个蓝图，查看员工表
emp_list_view = EmployeeListView.as_view('emp_list')
admin.add_url_rule('/emp/list/', view_func= emp_list_view,defaults={'page': 1})
admin.add_url_rule('/emp/list/<int:page>/', view_func=emp_list_view )

#注册一个蓝图，删除一个员工
admin.add_url_rule('/emp/del/<id>', view_func=EmployeeDelView.as_view('emp_del'))

#新增员工
# admin.add_url_rule('/emp/create/', view_func=EmployeeCreatView.as_view('emp_create'))

#添加员工信息
admin.add_url_rule('/emp/create/', view_func=EmployeeCreatOrEdit.as_view('emp_create'))
#编辑员工信息
admin.add_url_rule('/emp/edit/<id>/', view_func=EmployeeCreatOrEdit.as_view('emp_edit'))
















