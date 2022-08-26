from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from users.models import Employee
from users.serializer import EmployeeSerializer

# Create your views here.
class Login(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        data = Employee.objects.filter(email=email, password=password).values()
        if len(data) == 0:
            return Response({ "error": "Invalid email or password" }, status=status.HTTP_400_BAD_REQUEST)
        return Response(data[0], status=status.HTTP_200_OK)

class Register(APIView):
    def check_email(self, email):
        return Employee.objects.filter(email = email).values()

    def post(self, request):
        employee = self.check_email(request.data["email"])
        if len(employee) > 0:
            return Response({ "error": "Email already Exist" }, status=status.HTTP_400_BAD_REQUEST)
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListEmployees(APIView):
    def get(self, request):
        users = Employee.objects.all().values('id', 'name', 'email', 'description', 'position', 'hiring_date')
        return Response({
            "users": users
        }, status=status.HTTP_200_OK) 


class UpdateEmployees(APIView):
    def put(self, request):
        data = request.data
        print("Data: ", data)
        for detail in data:
            Employee.objects.filter(id=detail['id']).update(
                name=detail['name'],
                description = detail['description'],
                position = detail['position'],
            )

        return Response({
            "users": data
        }, status=status.HTTP_200_OK) 

class DeleteEmployee(APIView):
    def delete(self, request, id):
        Employee.objects.filter(id=id).delete()
        return Response({
            "result": "Employee Deleted Successfully"
        })