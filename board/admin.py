from django.contrib import admin
from .models import SchoolRecord, Record, Test, TargetUniv, Question

# Register your models here.
admin.site.register(SchoolRecord)
admin.site.register(Record)
admin.site.register(Test)
admin.site.register(TargetUniv)
admin.site.register(Question)
