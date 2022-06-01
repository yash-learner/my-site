from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
  path('students/', views.list_students,),
  path('students/<str:pk>', views.list_student),
]
