# Generated by Django 4.1 on 2024-04-14 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_certifications_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='upath',
            field=models.CharField(max_length=500, null=True),
        ),
    ]