from rest_framework import serializers
from .models import VacationRequest

class VacationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationRequest
        fields = ['start_date', 'end_date', 'reason', 'file', 'status', 'emp_email']

