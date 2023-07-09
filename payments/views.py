from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment
from .serializer import PaymentSerializer, PaymentUpdateSerializer


class PaymentCreateView(APIView):
    @swagger_auto_schema(
        request_body=PaymentSerializer,
        responses={"200": PaymentSerializer, "400": "Bad Request"},
    )
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = Payment(**serializer.validated_data)
            payment.save()
            # Perform additional actions like sending Kafka events or notifications here
            return Response(
                PaymentSerializer(payment).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentUpdateView(APIView):
    @swagger_auto_schema(
        responses={"200": PaymentSerializer, "400": "Bad Request"},
    )
    def get(self, request, payment_id):
        try:
            payment = Payment.objects.get(id=payment_id, is_active=True)
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=PaymentUpdateSerializer,
        responses={"200": PaymentSerializer, "400": "Bad Request"},
    )
    def put(self, request, payment_id):
        try:
            payment = Payment.objects.get(id=payment_id, is_active=True)
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PaymentUpdateSerializer(data=request.data)
        if serializer.is_valid():
            payment.amount = serializer.validated_data["amount"]
            payment.save()
            return Response(PaymentSerializer(payment).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, payment_id):
        try:
            payment = Payment.objects.get(id=payment_id, is_active=True)
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND
            )

        payment.is_active = False
        payment.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
