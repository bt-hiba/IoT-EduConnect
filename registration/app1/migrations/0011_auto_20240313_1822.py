# Generated by Django 3.2.24 on 2024-03-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20240313_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='pdff',
        ),
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
