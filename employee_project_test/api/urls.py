from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.employee_view import EmployeeViewSet

app_name = "api"

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
