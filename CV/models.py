from django.db import models


# Create your models here.

class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

class Experience(models.Model):
    job_description = models.TextField(max_length=256)
    job_start_date = models.DateField()
    job_end_date = models.DateField()

    def __str__(self):
        return self.job_description