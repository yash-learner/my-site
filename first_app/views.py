from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from first_app.models import Student
# Create your views here.


def index(request):
  return render(request, 'first_app/example.html')


def variable_view(request):
  view_variable = {'first_name': 'Yaswanth', 'last_name': 'Bethu'}
  return render(request, 'first_app/variable.html', context=view_variable)

def list_students(request):
  all_students = Student.objects.all()
  context = {'students': all_students}
  return render(request, 'first_app/list.html', context=context)

def add_student(request):
  if request.POST:
    name = request.POST['name']
    age = int(request.POST['age'])
    branch = request.POST['branch']
    roll_no = int(request.POST['roll_no'])
    Student.objects.create(name=name, age=age, branch=branch, roll_no=roll_no)
    return redirect(reverse('first_app:list'))
  else:
    return render(request, 'first_app/add.html')

def delete_student(request):
  if request.POST:
    roll_no = request.POST['roll_no']
    try:
      Student.objects.get(roll_no=roll_no).delete()
      return redirect(reverse('first_app:list'))
    except :
      print(f'The student with roll number {roll_no} not found.')
      return redirect(reverse('first_app:list'))
  else:
    return render(request, 'first_app/delete.html')


def update_student(request, *args, **kwargs):
  all_students = Student.objects.all()
  context = {'students': all_students}
  print(args, kwargs)
  if len(kwargs) == 0:
    return render(request, 'first_app/update.html', context=context)
  elif request.POST:
    print(request.POST, kwargs)
    student = Student.objects.get(id=int(kwargs['id']))
    student.name = request.POST['name']
    student.age = int(request.POST['age'])
    student.branch = request.POST['branch']
    student.roll_no = int(request.POST['roll_no'])
    student.save()
    return redirect(reverse('first_app:list'))

  else:
    print("hello", kwargs)
    context = Student.objects.get(id=int(kwargs['id'])).__dict__
    print(context)
    return render(request, 'first_app/edit.html', context=context)
