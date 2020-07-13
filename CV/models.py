from django.db import models


# Create your models here.

class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class Experience(models.Model):
    job_title = models.TextField(max_length=256)
    job_description = models.TextField()
    job_company = models.TextField(max_length=256)
    job_start_date = models.DateField()
    job_end_date = models.DateField()

    def __str__(self):
        return self.job_title


class Education(models.Model):
    certificate_title = models.TextField(max_length=512)
    certificate_description = models.TextField()
    certificate_start_date = models.DateField()
    certificate_end_date = models.DateField()
    certificate_institute = models.TextField(max_length=256)

    def __str__(self):
        return self.certificate_title
