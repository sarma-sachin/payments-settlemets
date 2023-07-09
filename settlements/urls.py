from django.urls import path
from .views import (
    SettlementCreateView,
    SettlementUpdateView,
)

app_name = "settlements"

urlpatterns = [
    path("api/settlements/", SettlementCreateView.as_view(), name="settlement-create"),
    path(
        "api/settlements/<int:settlement_id>/",
        SettlementUpdateView.as_view(),
        name="settlement-details",
    ),
]
