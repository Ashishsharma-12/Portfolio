# Generated by Django 4.1 on 2024-04-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='subtitle',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
