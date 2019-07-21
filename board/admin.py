from django.contrib import admin
from .models import SchoolRecord, Test, TargetUniv

# Register your models here.
admin.site.register(SchoolRecord)
admin.site.register(Test)
admin.site.register(TargetUniv)
