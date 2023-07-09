from rest_framework import serializers


class SettlementSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    payment_ids = serializers.ListField(child=serializers.IntegerField())
    settled_amount = serializers.IntegerField()
