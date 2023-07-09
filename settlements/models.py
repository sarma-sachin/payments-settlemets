from djongo import models


class Settlement(models.Model):
    """Model definition for Settlement."""

    payment_ids = models.JSONField()
    settled_amount = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Settlement."""

        app_label = "settlements"
        verbose_name = "Settlement"
        verbose_name_plural = "Settlements"

    @property
    def amount_in_rupees(self):
        return f"{self.settled_amount/100:.2f}"

    def __str__(self):
        """Unicode representation of Settlement."""
        return f"{self.settled_amount}"

    # def save(self, *args, **kwargs):
    #     """Save method for Settlement."""
    #     self.full_clean()
    #     return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Settlement."""
        return ""
