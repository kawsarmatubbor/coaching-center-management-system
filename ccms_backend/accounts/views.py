from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
import requests

BULKSMS_API_URL = "http://bulksmsbd.net/api/smsapi"
API_KEY = "rYaSnqi7JB5T8o2LpDbH"
SENDER_ID = "8809617625166"


@api_view(['POST'])
def registration_view(request):
    serializer = serializers.RegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        phone_number = user.phone_number
        
        payload = {
            "api_key": API_KEY,
            "senderid": SENDER_ID,
            "number": phone_number,
            "message": "Welcome! Your registration was successful.",
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
