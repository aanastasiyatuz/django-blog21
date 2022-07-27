from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegisterSerializer

User = get_user_model()

@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Вы успешно зарегистрировались")
