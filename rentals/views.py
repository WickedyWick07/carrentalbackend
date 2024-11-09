from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Rental  # Import your Rental model
from .serializers import RentalSerializer  # Import your RentalSerializer



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_rental(request):
    serializer = RentalSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(user=request.user)  # Assign current authenticated user to 'user' field
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_rental(request):
    user = request.user
    rentals = Rental.objects.filter(user=user)
    serializer = RentalSerializer(rentals, many=True)

    return Response(serializer.data)
