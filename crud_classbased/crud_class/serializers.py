from pyexpat import model
from rest_framework import serializers
from .models import Student

class StudnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=['id','name','stream','mobile']
        read_only = (['id'])