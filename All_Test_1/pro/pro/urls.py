"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('student/<str:regno>/', views.student_profile, name='student_profile'),
    path('employee/<str:empid>/<str:role>/', views.employee_profile, name='employee_profile'),
    path('update_profile/<int:adno>/', views.updata_student, name='update_profile'),
    path('mentors/<str:empid>/<str:role>/', views.mentor_allocate, name='mentors'),
    path('get_regno/', views.get_regno, name='get_regno'),
    path('save_ment_data/', views.save_ment_data, name='save_ment_data'),
    path('ipt_companies/<str:empid>/<str:role>', views.ipt_companies_view, name='ipt_companies'),
    path('approve_student/<int:ipdid>/', views.approve_student, name='approve_student'),
    path('logout/',views.logout,name='logout'),
    path('ipt_status/<str:empid>/<str:role>/', views.iptstatus, name='ipt_status'),
    path('placenment/<str:empid>/<str:role>/',views.placenment,name='Placenment'),
    path('save_data_placenment/<str:empid>/<str:role>/', views.save_data_placenment, name='save_data_placenment'),
    path('placenmentstd/<str:empid>/<str:role>/', views.placenment_data, name='Placenmentstd'),
    path('get_regno_placenment/', views.get_regno_placnenment, name='get_regno_placenment'),
    path('save_placenment_data/', views.save_placenment_data, name='save_placenment_data'),
    path('views/<str:empid>/<str:role>',views.viewsf,name='views'),
    path('download-csv/', views.download_csv, name='download_csv'),
    path('placement_csv/<str:pcid>/', views.placenement_csv, name='placement_csv'),
    path('fetch_companies/', views.fetch_companies, name='fetch_companies'),
    path('fetch_pcode/', views.fetch_pcode, name='fetch_pcode'),




]

