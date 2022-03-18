from flask_wtf import Form
import wtforms

#作用：在后台数据库实例和前台表单之间的桥梁
class EmployeeForm(Form):
    name = wtforms.StringField('姓名')
    gender = wtforms.RadioField('性别',choices=[('男','男'),('女','女')],default='男')   #单选项
    job = wtforms.StringField('工作', default='工程师')  #default是默认选项
    birthdate = wtforms.DateField('生日')
    idcard = wtforms.StringField('IDcard')
    address = wtforms.StringField('地址')
    salary = wtforms.DecimalField('工资')     #浮点数
    # department_id = wtforms.SelectField('部门', choices=[(1,'财务部'),(2,'测试部')])   #下拉选项
    depaitment_id = wtforms.SelectField('部门')   #下拉选项

