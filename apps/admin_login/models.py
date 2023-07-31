from django.db import models
from django.contrib.auth.models import User

#third party imports
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class Level(models.Model):
    MANAGEMENT = 1
    MANAGER = 2
    KADEP = 3
    SPV = 4
    STAFF = 5

    LEVELS = [
        (MANAGEMENT, "management"),
        (MANAGER, "manager"),
        (KADEP, "kepala departemen"),
        (SPV, "supervisor"),
        (STAFF, "staff")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipe = models.IntegerField(
        choices=LEVELS, default=STAFF, blank=True, null=True    
    )

    class Meta:
        app_label = "admin_login"
        verbose_name = "Level"
        verbose_name_plural = "Level"

class Departemen(models.Model):
    HR = 1
    RND = 2
    MARKETING = 3
    FINANCE = 4
    INVENTORY = 5

    DEPARTEMEN = [
        (HR,"Human Resources"),
        (RND, "Research And Development"),
        (MARKETING, "Marketing"),
        (FINANCE, "Finance"),
        (INVENTORY, "Inventory")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_departemen = models.IntegerField(choices=DEPARTEMEN,blank=True,null=True)


class StaffProfile(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.CASCADE
    )
    full_name = models.CharField(blank=True, null=True, max_length=100)
    nik = models.CharField(blank=True, null=True,max_length=100)