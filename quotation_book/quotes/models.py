from django.db import models


class Authors(models.Model):
    fullname = models.CharField(max_length=60, null=False, unique=True)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=100)
    description = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class Quotes(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    quote = models.TextField()
