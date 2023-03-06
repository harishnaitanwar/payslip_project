from django.contrib import admin
from Employee_data.models import EmployeeData,EmployeeSalary,Expenses
# Register your models here.
admin.site.register(EmployeeData)
admin.site.register(EmployeeSalary)
admin.site.register(Expenses)