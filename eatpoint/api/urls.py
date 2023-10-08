from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.establishments import EstablishmentViewSet, ReviewViewSet
from api.views.user import (
    SignUp,
    TokenView,
    UserView,
)

router = DefaultRouter()

router.register(
    "establishments", EstablishmentViewSet, basename="establishments"
)
router.register(
    r"establishment/(?P<establishment_id>\d+)/reviews",
    ReviewViewSet,
    basename="review",
)
router.register("users", UserView),

urlpatterns = [
    path("v1/auth/signup/", SignUp.as_view()),
    path("v1/auth/token/", TokenView.as_view()),
    path("v1/", include(router.urls)),
]
