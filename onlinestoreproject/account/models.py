from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomAccountManager(BaseUserManager):

    def create_user(self, username, email, password, **other_fields):
        if not username:
            raise ValueError("You must provide a username")
        if not email:
            raise ValueError("You must provide a email")
        
        user_email = email.lower()
        # print("This is the email:", user_email)
        user = self.model(username=username, email=user_email, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have staff status")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have superuser status")
        if other_fields.get('is_active') is not True:
            raise ValueError("Superuser must have active status")

        return self.create_user(username, email, password, **other_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# @receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
# def delete_auth_token(sender, instance, using, **kwargs):
#     try:
#         Token.objects.get(user=instance).delete()
#     except Exception as e:
#         print("Error. Maybe token was created usign drf for this user", e)