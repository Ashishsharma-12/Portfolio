# Generated by Django 4.1 on 2024-04-12 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_projects_subtitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='proefficient',
            new_name='level',
        ),
    ]
