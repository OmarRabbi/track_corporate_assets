from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='checked_out_devices')
    checked_out_at = models.DateTimeField()
    checked_in_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='checked_in_devices')
    checked_in_at = models.DateTimeField(null=True)
    condition_when_checked_out = models.TextField()
    condition_when_checked_in = models.TextField(null=True)
    def __str__(self):
        return f"{self.asset} - Checked out by {self.checked_out_by} at {self.checked_out_at}"