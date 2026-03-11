from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'nit', 'city', 'phone', 'email', 'employee_count', 'created_at']

    def get_employee_count(self, obj):
        return obj.employees.count()


class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Employee
        fields = [
            'id', 'company', 'company_name', 'first_name', 'last_name',
            'document_number', 'email', 'phone', 'position', 'department',
            'gender', 'hire_date', 'status', 'created_at', 'updated_at'
        ]


class EmployeeListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'document_number', 'position', 'company_name', 'status']