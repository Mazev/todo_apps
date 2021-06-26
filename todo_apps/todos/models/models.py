from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=30)
    state = models.BooleanField(default=False)
    person_responsible = models.CharField(max_length=50, null=True)


class Person(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = 'people'


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'
