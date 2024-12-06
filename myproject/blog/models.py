from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name