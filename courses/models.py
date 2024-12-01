from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    igredients = models.TextField()
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    max_students = models.IntegerField()

    def __str__(self):
        return self.title