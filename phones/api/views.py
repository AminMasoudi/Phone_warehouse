from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import PhoneSerializer

class NewPhoneAPI(APIView):
    # authentication_classes = SessionAuthentication
    # permission_classes = IsAuthenticated

    def post(self, requests, *args, **kwargs):
        form = PhoneSerializer(data=requests.data)
        form.is_valid(raise_exception=True)
        form.save()
