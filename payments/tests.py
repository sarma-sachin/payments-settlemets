from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Payment


User = get_user_model()


class PaymentAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email="sender@gmail.com", password="password", is_customer=True
        )
        self.user2 = User.objects.create_user(
            email="recipient@gmail.com", password="password", is_customer=False
        )
        self.payment = Payment.objects.create(
            sender=self.user1, recipient=self.user2, amount=100
        )

    def test_create_payment(self):
        url = reverse("payments:payment-create")
        data = {
            "sender_id": self.user1.pk,
            "recipient_id": self.user2.pk,
            "amount": 200,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 2)

    def test_update_payment(self):
        url = reverse("payments:payment-details", args=[self.payment.pk])
        data = {"amount": 150}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payment.refresh_from_db()
        self.assertEqual(self.payment.amount, 150.0)

    def test_delete_payment(self):
        url = reverse("payments:payment-details", args=[self.payment.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Payment.objects.filter(pk=self.payment.pk, is_active=True).exists()
        )

    def test_retrieve_payment(self):
        url = reverse("payments:payment-details", args=[self.payment.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "id": self.payment.pk,
            "sender_id": self.payment.sender.pk,
            "recipient_id": self.payment.recipient.pk,
            "amount": self.payment.amount,
        }
        self.assertEqual(response.data, expected_data)
