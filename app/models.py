

from django.db import models

from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    friends = models.ManyToManyField('self')
