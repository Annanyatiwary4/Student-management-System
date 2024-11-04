from django.urls import path,include
from . import views

urlpatterns = [
path('FacultyHomepage/', views.FacultyHomepage, name='FacultyHomepage'),
path('Blog/', views.Blog, name='Blog'),
path('add_post/', views.add_post, name='add_post'),
path(' view_posts/', views. view_posts, name=' view_posts'),
path('add_course/',views.add_course,name='add_course'),
path('view_student_list/',views.view_student_list,name='view_student_list'),
path('post_marks/',views.post_marks,name='post_marks'),
]