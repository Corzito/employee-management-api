from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer, EmployeeListSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'nit', 'city']
    ordering_fields = ['name', 'created_at']


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('company').all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['company', 'status', 'department', 'gender']
    search_fields = ['first_name', 'last_name', 'document_number', 'email', 'position']
    ordering_fields = ['last_name', 'hire_date', 'created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return EmployeeListSerializer
        return EmployeeSerializer

    @action(detail=False, methods=['get'])
    def active(self, request):
        active_employees = Employee.objects.filter(status='active').select_related('company')
        serializer = EmployeeListSerializer(active_employees, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_company(self, request):
        company_id = request.query_params.get('company_id')
        if not company_id:
            return Response({'error': 'company_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        employees = Employee.objects.filter(company_id=company_id).select_related('company')
        serializer = EmployeeListSerializer(employees, many=True)
        return Response(serializer.data)