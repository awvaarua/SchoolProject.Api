from django.db import models
from django.contrib.auth.models import User
from .department import Department

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return self.user.first_name
