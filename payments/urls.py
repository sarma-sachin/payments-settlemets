from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentUpdateView,
)

app_name = "payments"

urlpatterns = [
    path("api/payments/", PaymentCreateView.as_view(), name="payment-create"),
    path(
        "api/payments/<int:payment_id>/",
        PaymentUpdateView.as_view(),
        name="payment-details",
    ),
]
