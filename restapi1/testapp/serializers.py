from rest_framework import serializers
from .models import Employee

class EmployeeSerializers(serializers.Serializer):
    ename=serializers.CharField(max_length=64)
    eaddr=serializers.CharField(max_length=64)
    esal=serializers.IntegerField()
    eno=serializers.IntegerField()
    def create(self,kwargs):
        return Employee.objects.create(**kwargs)
