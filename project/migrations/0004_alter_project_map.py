# Generated by Django 5.1.3 on 2024-11-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='map',
            field=models.ImageField(blank=True, null=True, upload_to='map_images', verbose_name='Thumbnail'),
        ),
    ]