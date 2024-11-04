from django.urls import path, include
from . import views

urlpatterns = [
path('', views.studentHomepage, name='studentHomepage'),
]