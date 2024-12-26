"""Payment_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Employee_data.views import home, employeeDetails,getEmployeeById,Salary,ExpensesCompany,my_view
from django.conf.urls.static import static
from django.conf import settings
from .settings import MEDIA_URL,MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('employee/',employeeDetails,name="empdetails"),
    path('getemp/',getEmployeeById.as_view(),name='getemp'),
    path('salary/',Salary,name="salary"),
    path('addexpenses/',ExpensesCompany.as_view(),name='addexpenses'),
    path('status/',ExpensesCompany.as_view(),name='status'),
    path('myview/',my_view.as_view(),name='myview'),

]
urlpatterns += static(MEDIA_URL,
                      document_root=MEDIA_ROOT)




texted
