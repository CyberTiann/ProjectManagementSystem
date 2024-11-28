# Generated by Django 5.1.3 on 2024-11-27 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='document',
            field=models.FileField(blank=True, help_text='PDF/DOCX/XLSX etc', null=True, upload_to='project_documents'),
        ),
    ]