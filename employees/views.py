from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Department, Employee, Attendance, Performance
from .serializers import DepartmentSerializer, EmployeeSerializer, AttendanceSerializer, PerformanceSerializer

class DashboardView(TemplateView):
    template_name = "employees/dashboard.html"

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'email']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'status', 'date']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'rating']
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
