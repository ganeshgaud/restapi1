from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import EmployeeSerializers
from django.http import HttpResponse
from django.views import View
import io
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializers(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        emp=Employee.objects.all()
        serializer=EmployeeSerializers(emp,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=EmployeeSerializers(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Employee details added Successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        msg={'msg':'Enter Valid Employee details'}
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializers(emp,data=pdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Employee details updated Successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')



    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp=Employee.objects.get(id=id)
        emp.delete()
        msg={'msg':'Employee deleted Successfully'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')
