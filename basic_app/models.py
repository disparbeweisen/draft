from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length = 256, unique = True)


    def __str__(self):
        return self.company_name


class Jobs(models.Model):
    company_topic = models.ForeignKey(Company, on_delete = models.DO_NOTHING)
    job_name = models.CharField(max_length = 256, unique = True)
    more_info = models.URLField(unique = True)

    def __str__(self):
        return self.job_name
