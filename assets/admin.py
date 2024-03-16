from django.contrib import admin
from .models import Company, Employee, Asset, DeviceLog
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Asset)
admin.site.register(DeviceLog)
