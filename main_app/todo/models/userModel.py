from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the User model.

    Provides methods for creating regular users and superusers.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.

        Args:
            email (str): The user's email address.

            password (str): The user's password.
            
            extra_fields: Additional user fields.

        Returns:
            User: The created user object.
        """

        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.

        Args:
            email (str): The superuser's email address.

            password (str): The superuser's password.

            extra_fields: Additional user fields.

        Returns:
            User: The created superuser object.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        # extra_fields.setdefault("email_confirmed", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=60, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    REQUIRED_FIELDS = ["email", "name", "password"]
    USERNAME_FIELD = "username"

    def __str__(self) -> str:
        return self.name