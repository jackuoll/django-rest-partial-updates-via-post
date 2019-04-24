from django.db import models


class Test(models.Model):
    subscriber_key = models.CharField(max_length=50, primary_key=True)
    direct = models.CharField(max_length=50)
    methods = models.CharField(max_length=50)
