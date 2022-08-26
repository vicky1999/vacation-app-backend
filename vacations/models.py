from django.db import models

from users.models import Employee

# Create your models here.
class VacationRequest(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    file = models.TextField()
    status = models.TextField(default='PENDING')
    emp_email = models.EmailField()

    def __str__(self):
        return self.id
