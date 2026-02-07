from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    number=models.CharField(max_length=10)

    def __str__(self):
        return self.name
