from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    description = models.TextField()
    position = models.TextField()
    hiring_date = models.DateField()

    def __str__(self):
        return str(self.id)




