from django.contrib import admin
from .models import Category, Project, Status, Year
# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Status)
admin.site.register(Year)