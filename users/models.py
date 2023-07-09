from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Model definition for CustomUser."""

    email = models.EmailField(help_text=_("Email Address"), unique=True)
    is_customer = models.BooleanField(
        help_text=_("User is Customer/Merchant"), default=True
    )
    is_staff = models.BooleanField(help_text=_("User is Staff or not"), default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = CustomUserManager()

    class Meta:
        """Meta definition for CustomUser."""

        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"

    def __str__(self):
        """Unicode representation of CustomUser."""
        return f"{self.email}"

    def save(self, *args, **kwargs):
        """Save method for CustomUser."""
        self.full_clean()
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for CustomUser."""
        return ""
