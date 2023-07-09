from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Payment

User = get_user_model()


class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sender_id = serializers.IntegerField()
    recipient_id = serializers.IntegerField()
    amount = serializers.IntegerField()

    def validate(self, data):
        sender_id = data.get("sender_id")
        recipient_id = data.get("recipient_id")
        errors = {}

        if not User.objects.filter(is_customer=True, pk=sender_id).exists():
            errors["sender_id"] = "Sender must be a Customer."
        if User.objects.filter(is_customer=True, pk=recipient_id).exists():
            errors["recipient_id"] = "Recipient must be a Merchant."

        if errors:
            raise serializers.ValidationError(errors)

        return data


class PaymentUpdateSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
