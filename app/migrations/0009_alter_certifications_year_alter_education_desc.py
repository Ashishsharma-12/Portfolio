# Generated by Django 4.1 on 2024-04-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_education_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifications',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='desc',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
