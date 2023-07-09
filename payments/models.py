from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class Payment(models.Model):
    """Model definition for Payment."""

    sender = models.ForeignKey(
        help_text=_("User sending money in the transaction"),
        to=User,
        on_delete=models.CASCADE,
        related_name="sent_payments",
    )
    recipient = models.ForeignKey(
        help_text=_("User recieving money in the transaction"),
        to=User,
        on_delete=models.CASCADE,
        related_name="received_payments",
    )
    amount = models.PositiveIntegerField(help_text=_("Amount in the payment in paisa"))
    is_active = models.BooleanField(
        help_text=_("Indicate the payment is active or deleted."), default=True
    )
    is_settled = models.BooleanField(
        help_text=_("Indicate the payment is settled or not."), default=True
    )
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Payment."""

        app_label = "payments"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    @property
    def amount_in_rupees(self):
        return f"{self.amount/100:.2f}"

    def __str__(self):
        """Unicode representation of Payment."""
        return f"{self.sender_id} send {self.amount_in_rupees} to {self.recipient_id}"

    def clean(self):
        errors = {}
        if not User.objects.filter(is_customer=True, id=self.sender_id):
            errors["sender"] = _("Sender must be a Customer.")
        if not User.objects.filter(is_customer=False, id=self.recipient_id):
            errors["recipient"] = _("Recipient must be a Merchant.")
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        """Save method for Payment."""
        self.full_clean()
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Payment."""
        return ""
