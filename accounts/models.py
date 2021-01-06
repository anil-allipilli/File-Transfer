from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse
import random
import os
from accounts.tasks import send_staff_email_task


class MyUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        first_name,
        last_name,
        phone_number,
        company_name,
        company_logo,
        password=None,
    ):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            company_name=company_name,
            company_logo=company_logo,
            is_active=False,
        )
        print(user.email)
        user.set_password(password)
        user.save(using=self._db)
        full_name = first_name + " " + last_name

        send_staff_email_task.delay(full_name, company_name, email)
        return user

    def create_superuser(
        self, email, first_name, last_name, phone_number, company_name, password=None
    ):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            company_name=company_name,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    company_name = models.CharField(max_length=150, blank=True)
    company_logo = models.ImageField(upload_to="logos/", blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "company_name"]

    objects = MyUserManager()

    def get_absolute_url(self):
        return reverse("user-detail", kwargs={"pk": self.pk})

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        return self.get_full_name()