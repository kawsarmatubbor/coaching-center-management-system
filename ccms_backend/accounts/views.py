from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from . import serializers
import requests

BULKSMS_API_URL = "http://bulksmsbd.net/api/smsapi"
API_KEY = "rYaSnqi7JB5T8o2LpDbH"
SENDER_ID = "8809617625166"


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registration_view(request):
    if request.user.role == "admin":
        serializer = serializers.RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            phone_number = user.phone_number
            first_name = user.first_name
            last_name = user.last_name
            
            payload = {
                "api_key": API_KEY,
                "senderid": SENDER_ID,
                "number": phone_number,
                "message": f"প্রিয় {first_name} {last_name},\nপাঠশালা কোচিং সেন্টারে তোমাকে স্বাগতম। \n-পাঠশালা কোচিং সেন্টার",
            }

            try:
                response = requests.post(BULKSMS_API_URL, data=payload)
                
                try:
                    sms_response = response.json()
                except ValueError:
                    sms_response = {"raw_response": response.text}

                return Response(
                    {
                        "user": serializer.data,
                        "sms_response": sms_response
                    },
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response({
            "error": "Authentication credentials were not provided."
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    serializer = serializers.UserSerializer(user)
    return Response(serializer.data)
