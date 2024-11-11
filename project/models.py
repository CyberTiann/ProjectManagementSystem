from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Status(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name
    
class Year(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Years'

    def __str__(self):
        return self.name
    
class Project(models.Model):
    year = models.ForeignKey(Year, related_name='project', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, related_name='project', on_delete=models.CASCADE)
    map = models.ImageField(upload_to='map_images', blank=True, null=True, verbose_name="Thumbnail")
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='project', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    project_cost = models.CharField(blank=True, null=True, max_length=255)
    status = models.ForeignKey(Status, related_name='project', on_delete=models.CASCADE, null=True, blank=True)
    started = models.DateField()
    contact = models.CharField(max_length=255, null=True, blank=True)
    update = models.TextField(blank=True, null=True)
    document = models.FileField(upload_to='project_documents', blank=True, null=True, help_text="PDF/DOCX/XLSX etc")
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name
    
