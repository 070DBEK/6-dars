from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1,)
    address = models.CharField(max_length=100,)

    def __str__(self):
        return f"{self.first_name},{self.last_name}"