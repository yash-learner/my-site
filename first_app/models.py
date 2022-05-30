from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  branch = models.CharField(max_length=30)
  roll_no = models.IntegerField()

  def __str__(self):
    return f"The student details are: {self.name}, {self.age}, {self.branch}, {self.roll_no}"
