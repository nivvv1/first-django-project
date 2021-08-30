from django.shortcuts import render

from  django.shortcuts import HttpResponse
from  django.shortcuts import get_object_or_404
from rest_framework.views import APIViews
from rest_framework.response import Response

from rest_framework import status
from . models import employees
from . serializers import employeeSerializer

class employeeList(APIViews):
    

    def get(self,request):
        employee1=employees.objects.all()
        serializer=employeeSerializer(employee1,many=True)
        return Response(serializer.data)



    def post(self):
        pass
    

