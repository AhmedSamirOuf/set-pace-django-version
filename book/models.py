from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30, default='samir')
    publisher = models.CharField(max_length=100, default='samir')
    vendors = models.TextField(null=True, max_length=30)
    types = models.TextField(null=True, max_length=15)
    category = models.CharField(max_length=15, default='thriller')
