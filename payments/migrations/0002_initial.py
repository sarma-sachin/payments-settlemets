# Generated by Django 4.1.10 on 2023-07-09 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="recipient",
            field=models.ForeignKey(
                help_text="User recieving money in the transaction",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_payments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="sender",
            field=models.ForeignKey(
                help_text="User sending money in the transaction",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sent_payments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]