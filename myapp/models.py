from django.db import models
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.ename     

