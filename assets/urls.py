from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 
# URL patterns for Django views
urlpatterns = [    
    path('company-list/', views.company_list, name='company_list'),
    path('add-company/', views.add_company, name='add_company'),
    path('company/<int:company_id>/update/', views.update_company, name='update_company'),
    path('company/<int:company_id>/delete/', views.delete_company, name='delete_company'),
    
    path('employee-list/', views.employee_list, name='employee_list'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('employee/<int:employee_id>/update/', views.update_employee, name='update_employee'),
    path('employee/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),

    path('asset-list/', views.asset_list, name='asset_list'),
    path('add-asset/', views.add_asset, name='add_asset'),
    path('asset/<int:asset_id>/update/', views.update_asset, name='update_asset'),
    path('asset/<int:asset_id>/delete/', views.delete_asset, name='delete_asset'),

    path('device-log-list/', views.device_log_list, name='device_log_list'),
    path('add-device-log/', views.add_device_log, name='add_device_log'),
    path('device_log/<int:device_log_id>/update/', views.update_device_log, name='update_device_log'),
    path('device_log/<int:device_log_id>/delete/', views.delete_device_log, name='delete_device_log'),
]