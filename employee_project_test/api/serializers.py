from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = [ "first_name",
                    "last_name",
                    "email",
                     "phone_number",
                    "position",
                    "salary",
                    "date_hire"]