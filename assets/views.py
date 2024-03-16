from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from django.db import IntegrityError
from .models import Company, Employee, Asset, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, AssetSerializer, DeviceLogSerializer
# Create your views here.

# Viewsets for REST API
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

# Views for rendering templates
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def add_company(request):
    if request.method == 'POST':
        name = request.POST.get('companyName')  # Corrected parameter name
        if name:
            try:
                Company.objects.create(name=name)
            except IntegrityError as e:
                return render(request, 'add_company.html', {'error_message': str(e)})
            return redirect('company_list')  # Redirect to company list after adding
        else:
            return render(request, 'add_company.html', {'error_message': 'Company name cannot be empty'})
    else:
        return render(request, 'add_company.html')
    
def update_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        new_name = request.POST.get('company_name')  # Assuming the form field name is 'company_name'
        company.name = new_name
        company.save()
        return redirect('company_list')
    else:
        return render(request, 'update_company.html', {'company': company})

def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    else:
        return render(request, 'confirm_delete_company.html', {'company': company})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('employeeName')
        company_id = request.POST.get('companyId')
        company = get_object_or_404(Company, id=company_id)
        Employee.objects.create(name=name, company=company)
        return redirect('employee_list')  # Corrected the redirect name
    else:
        companies = Company.objects.all()  # Fetch companies for the dropdown
        return render(request, 'add_employee.html', {'companies': companies})

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    companies = Company.objects.all()  # Retrieve all companies
    if request.method == 'POST':
        new_name = request.POST.get('employee_name')  # Assuming the form field name is 'employee_name'
        company_id = request.POST.get('company_id')  # Retrieve the selected company ID from the form
        company = get_object_or_404(Company, id=company_id)  # Get the Company object based on the selected ID
        employee.name = new_name
        employee.company = company  # Assign the selected company to the employee
        employee.save()
        return redirect('employee_list')
    else:
        return render(request, 'update_employee.html', {'employee': employee, 'companies': companies})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    else:
        return render(request, 'confirm_delete_employee.html', {'employee': employee})

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})

def add_asset(request):
    if request.method == 'POST':
        name = request.POST.get('assetName')
        description = request.POST.get('assetDescription')
        assigned_to_id = request.POST.get('assigned_to_id')
        assigned_to = get_object_or_404(Employee, id=assigned_to_id)
        Asset.objects.create(name=name, description=description, assigned_to=assigned_to)
        return redirect('asset_list')  # Corrected the redirect name
    else:
        employees = Employee.objects.all()  # Fetch employees for the dropdown
        return render(request, 'add_asset.html', {'employees': employees})

def update_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        new_name = request.POST.get('asset_name')  # Assuming the form field name is 'asset_name'
        new_description = request.POST.get('asset_description')  # Assuming the form field name is 'asset_description'
        asset.name = new_name
        asset.description = new_description
        asset.save()
        return redirect('asset_list')
    else:
        return render(request, 'update_asset.html', {'asset': asset})

def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    else:
        return render(request, 'confirm_delete_asset.html', {'asset': asset})

def device_log_list(request):
    device_logs = DeviceLog.objects.all()
    return render(request, 'device_log_list.html', {'device_logs': device_logs})

def add_device_log(request):
    if request.method == 'POST':
        asset_id = request.POST.get('asset_id')
        checked_out_by_id = request.POST.get('checked_out_by_id')
        checked_out_at = request.POST.get('checked_out_at')
        condition_when_checked_out = request.POST.get('condition_when_checked_out')

        asset = get_object_or_404(Asset, id=asset_id)
        checked_out_by = get_object_or_404(Employee, id=checked_out_by_id)
        
        DeviceLog.objects.create(
            asset=asset,
            checked_out_by=checked_out_by,
            checked_out_at=checked_out_at,
            condition_when_checked_out=condition_when_checked_out
        )
        return redirect('device_log_list')  # Corrected the redirect name
    else:
        assets = Asset.objects.all()  # Fetch assets for the dropdown
        employees = Employee.objects.all()  # Fetch employees for the dropdown
        return render(request, 'add_device_log.html', {'assets': assets, 'employees': employees})

from .models import Asset

def update_device_log(request, device_log_id):
    device_log = get_object_or_404(DeviceLog, id=device_log_id)
    employees = Employee.objects.all()
    assets = Asset.objects.all()
    if request.method == 'POST':
        checked_out_by_id = request.POST.get('checked_out_by_id')
        checked_out_at = request.POST.get('checked_out_at')
        checked_in_by_id = request.POST.get('checked_in_by_id')
        checked_in_at = request.POST.get('checked_in_at')
        condition_when_checked_out = request.POST.get('condition_when_checked_out')
        condition_when_checked_in = request.POST.get('condition_when_checked_in')
        asset_id = request.POST.get('asset_id')

        device_log.checked_out_by_id = checked_out_by_id
        device_log.checked_out_at = checked_out_at
        device_log.checked_in_by_id = checked_in_by_id
        device_log.checked_in_at = checked_in_at
        device_log.condition_when_checked_out = condition_when_checked_out
        device_log.condition_when_checked_in = condition_when_checked_in
        device_log.asset_id = asset_id

        device_log.save()
        return redirect('device-log-list')
    else:
        checked_in_by_id = device_log.checked_in_by_id
        checked_in_at = device_log.checked_in_at.strftime('%Y-%m-%dT%H:%M') if device_log.checked_in_at else ''
        condition_when_checked_in = device_log.condition_when_checked_in
        return render(request, 'update_device_log.html', {'device_log': device_log, 'employees': employees, 'assets': assets, 'checked_in_by_id': checked_in_by_id, 'checked_in_at': checked_in_at, 'condition_when_checked_in': condition_when_checked_in})

def delete_device_log(request, device_log_id):
    device_log = get_object_or_404(DeviceLog, id=device_log_id)
    if request.method == 'POST':
        device_log.delete()
        return redirect('device_log_list')
    else:
        return render(request, 'confirm_delete_device_log.html', {'device_log': device_log})