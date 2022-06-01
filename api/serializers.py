from rest_framework import serializers
from .models import StudentApi

class StudentApiSerializer(serializers.ModelSerializer):
  class Meta:
    model = StudentApi
    fields = ('id', 'name', 'roll_no')
