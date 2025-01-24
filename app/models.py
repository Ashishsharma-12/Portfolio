from django.db import models

# Create your models here.

class Skills_Library(models.Model):
    skill = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.skill

class Projects(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'pics')
    subtitle = models.CharField(max_length=500, null=True)
    upath = models.CharField(max_length=500, default= '#')

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    desc = models.CharField(max_length=500, null=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.degree

class Work_Experience(models.Model):
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    job_desc = models.TextField()

    def __str__(self):
        return self.company

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    msg = models.TextField()

    def __str__(self):
        return self.name

class Certifications(models.Model):
    certificate = models.CharField(max_length=100)
    organization = models.CharField(max_length=500)
    year = models.IntegerField()
    link = models.URLField(null=True)
    img = models.ImageField(upload_to = 'pics', null=True)

    def __str__(self):
        return self.certificate





















