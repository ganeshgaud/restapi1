from rest_framework import serializers
from .models import Employee
#By using Validators
def multiples_of_1000(value):
    if value%1000 != 0:
        raise serializers.ValidationError('Salary Should be multiples of 1000')
    return value

class EmployeeSerializers(serializers.Serializer):
    ename=serializers.CharField(max_length=64)
    eaddr=serializers.CharField(max_length=64)
    esal=serializers.IntegerField(validators=[multiples_of_1000,])
    eno=serializers.IntegerField()

#field level validation
    def validate_esal(self,value):
        if value<5000:
            raise serializers.ValidationError('Salary should be greater than 5000')
        return value


# Object level validation
    def validate(self,data):
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower()=='arnav':
            if esal>15000:
                raise serializers.ValidationError('Salary should not be greater than 5000')
        return data


    def create(self,kwargs):
        return Employee.objects.create(**kwargs)
    def update(self,instance,validated_data):
        instance.ename=validated_data.get('ename',instance.ename)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eno=validated_data.get('eno',instance.eno)
        instance.save()
        return instance
