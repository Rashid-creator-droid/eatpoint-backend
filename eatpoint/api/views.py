from django.conf import settings
from django.core.mail import send_mail
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .permissions import IsAdmin, IsSuperUser, IsUser
from .serializers import (
    MeSerializer,
    SignUpSerializer,
    TokenSerializer,
    UserSerializer,
)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("email",)
    lookup_field = "email"
    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = (IsAdmin | IsSuperUser,)

    @action(
        url_path="me",
        methods=["get", "patch"],
        detail=False,
        permission_classes=(IsUser,),
    )
    def me(self, request):
        serializer_class = MeSerializer
        if request.method == "GET":
            serializer = serializer_class(request._user, many=False)
            return Response(serializer.data)

        if request.method == "PATCH":
            user = User.objects.get(email=request._user)
            serializer = serializer_class(
                user, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class SignUp(APIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, created = User.objects.get_or_create(
            email=request.data.get("email"),
            is_active=False,
        )
        message = user.confirm_code
        user.confirmation_code = message
        user.save()

        send_mail(
            subject="Код подтверждения EatPoint",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[
                user.email,
            ],
            fail_silently=False,
        )

        if created:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class TokenView(APIView):
    serializer_class = TokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get("email")
        confirmation_code = request.data.get("confirmation_code")
        if not User.objects.filter(email=email).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = User.objects.get(email=email)
        if user.confirmation_code == confirmation_code:
            user.is_active = True
            user.save()
            return Response(
                {"token": user.token}, status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)
