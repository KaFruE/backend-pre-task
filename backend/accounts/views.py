from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from .serializers import (
    UserSignupSerializer,
    UserSigninSerializer
)


class UserSignupView(CreateAPIView):
    """
        API 예시
        POST localhost:8000/api/users/signup/
        {
            "email": "dwyug@gmail.com",
            "first_name": "dongwan",
            "last_name": "yug",
            "user_name": "dongwan yug",
            "password": "qlalfqjsgh!",
            "phone": "010-1234-6442",
            "gender": "MA",
            "birth_day": "1995-03-06"
        }
    """
    permission_classes = [AllowAny]
    serializer_class = UserSignupSerializer


class UserSigninView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class = UserSigninSerializer

    """
        API 예시
        POST localhost:8000/api/users/login/
        {
            "email" : "dwyug@gmail.com",
            "password" : "qlalfqjsgh!"
        }
    """
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserSignoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    """
        API 예시
        POST localhost:8000/api/users/logout/
    """
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist) as e:
            return Response({"message": "유저 정보가 없습니다."}, status=HTTP_400_BAD_REQUEST)

        return Response({"message": "로그아웃 되었습니다."}, status=HTTP_200_OK)