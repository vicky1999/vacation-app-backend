from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
from users.models import Employee
from vacations.models import VacationRequest

from vacations.serializer import VacationRequestSerializer

# Create your views here.
class Vacation(APIView):
    def post(self, request):
        folder = "uploads/"
        data = request.data
        data_file = data["file"]
        fs = FileSystemStorage(location=folder)
        filename = fs.save(data_file.name, data_file)
        file_url = fs.url(filename)
        employee = VacationRequest.objects.filter(emp_email=data["emp_email"])
        if len(employee) >= 4:
            return Response({
                "error": "only 4 Vacations can be requested"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        vacation_request = {
            "start_date": data["startDate"],
            "end_date": data["endDate"],
            "reason": data["reason"],
            "file": file_url,
            "status": "PENDING",
            "emp_email": data["emp_email"]
        }
        vacation_serializer = VacationRequestSerializer(data=vacation_request)
        if vacation_serializer.is_valid():
            vacation_serializer.save()
        else:
            return Response({
                "error": "Invalid data"
            }, status=status.HTTP_400_BAD_REQUEST)

        print(data)
        return Response({
            "result": "Vacation Saved Successfully"
        }, status=status.HTTP_200_OK)

    def get(self, request, pk):
        print("ID: ", pk)
        requests_list = VacationRequest.objects.filter(emp_email=pk).values();
        return Response({
            "data": requests_list
        }, status=status.HTTP_200_OK);

class VacationsList(APIView):
    def get(self, request):
        data = VacationRequest.objects.all().values()
        print("Data: ", data)
        return Response({
            "data": data
        }, status=status.HTTP_200_OK)

class UpdateStatus(APIView):
    def put(self, request):
        data = request.data
        print("Data: ", data)
        for detail in data:
            VacationRequest.objects.filter(id=detail['id']).update(status=detail['status'])
        
        return Response({
            "data": data
        }, status=status.HTTP_200_OK)

class DeleteVacation(APIView):
    def delete(self, request, id):
        VacationRequest.objects.filter(id=id).delete()
        return Response({
            "result": "Vacation Deleted Successfully"
        })
