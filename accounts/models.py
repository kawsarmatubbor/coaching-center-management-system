from django.db import models
from django.contrib.auth.models import AbstractUser
from . import manager

class CustomUser(AbstractUser):
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    username = None
    phone_number = models.CharField(max_length=14, unique=True)
    fathers_name = models.CharField(max_length=100)
    fathers_phone_number = models.CharField(max_length=14, blank=True, null=True)
    mothers_name = models.CharField(max_length=100)
    mothers_phone_number = models.CharField(max_length=14, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    date_of_birth = models.DateField(blank=True, null=True)
    present_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    s_class = models.CharField(max_length=50, blank=True, null=True)
    section = models.CharField(max_length=50, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile-pictures/',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = manager.CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.s_class or 'N/A'})"
