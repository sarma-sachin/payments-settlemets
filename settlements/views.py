from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Settlement
from .serializer import SettlementSerializer


class SettlementCreateView(APIView):
    @swagger_auto_schema(
        request_body=SettlementSerializer,
        responses={"200": SettlementSerializer, "400": "Bad Request"},
    )
    def post(self, request):
        serializer = SettlementSerializer(data=request.data)
        if serializer.is_valid():
            settlement = Settlement(**serializer.validated_data)
            settlement.save()
            return Response(
                SettlementSerializer(settlement).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SettlementUpdateView(APIView):
    @swagger_auto_schema(
        responses={"200": SettlementSerializer, "400": "Bad Request"},
    )
    def get(self, request, settlement_id):
        try:
            settlement = Settlement.objects.get(id=settlement_id)
        except Settlement.DoesNotExist:
            return Response(
                {"error": "Settlement not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = SettlementSerializer(settlement)
        return Response(serializer.data, status=status.HTTP_200_OK)
