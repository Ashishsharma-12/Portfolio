# Generated by Django 4.1 on 2024-04-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_certifications_img_certifications_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifications',
            name='img',
            field=models.FileField(null=True, upload_to='certs'),
        ),
    ]