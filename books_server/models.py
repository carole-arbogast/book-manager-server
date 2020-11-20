from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=60)
    cover = models.CharField(max_length=100, null=True, blank=True, default="")
    rating = models.IntegerField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    reading_status = models.CharField(choices=[("READ", "Read"), ("TO_READ", "To Read"), ("READING", "Reading")], max_length=10)
    bookshelf = models.ForeignKey("Bookshelf", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Bookshelf(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name