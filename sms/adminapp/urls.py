from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.Homepage, name='Homepage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randompagelogic/', views.randompagelogic, name='randompagelogic'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('loginpagecall', views.loginpagecall, name='loginpagecall'),
    path('registrationpagecall/', views.registrationpagecall, name='registrationpagecall'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/',views.logout,name='logout'),
    path('add_student/',views.add_student,name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('feedback_view/',views.feedback_view,name='feedback_view'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),


]