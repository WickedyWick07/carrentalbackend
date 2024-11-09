from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import PaymentForm
from .serializers import PaymentSerializer
from rentals.models import Rental
from rentals.serializers import RentalSerializer
from rest_framework.decorators import api_view, permission_classes

class RentalDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, rental_id):
        try:
            rental = Rental.objects.get(id=rental_id)
            serializer = RentalSerializer(rental)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Rental.DoesNotExist:
            return Response({'error': 'Rental not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payment_form(request, rental_id):
    try:
        rental = Rental.objects.get(id=rental_id)
    except Rental.DoesNotExist:
        return Response({'error': 'Rental not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, rental=rental)  # Save with user and rental
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)