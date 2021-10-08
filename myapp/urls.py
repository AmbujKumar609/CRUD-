from django.urls import path
from . import views

urlpatterns = [
    path('addstudent/',views.studentdata,name='addstudent')
]
