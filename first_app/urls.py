from django.urls import path
from . import views

app_name = 'first_app'
urlpatterns = [
  path('', views.index, name='index'),
  path('variable/', views.variable_view, name='variable'),
  path('list/', views.list_students, name='list'),
  path('add/', views.add_student, name='add'),
  path('delete/', views.delete_student, name='delete'),
  path('update/', views.update_student, name='update'),
  path('update/<int:id>/', views.update_student, name='update'),


]
