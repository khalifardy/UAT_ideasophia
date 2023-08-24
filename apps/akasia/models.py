from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class User(TimeStampedModel):
    id_asal = models.IntegerField(null=True)
    email = models.CharField(max_length=500, null=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    avatar = models.CharField(max_length=500)
    deleted_at = models.DateTimeField(null=True)
