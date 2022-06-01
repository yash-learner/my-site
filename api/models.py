from django.db import models

# Create your models here.
class StudentApi(models.Model):
  name = models.CharField(max_length=60)
  roll_no = models.CharField(max_length=60)


  def __str__(self):
    return self.name
