from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

# import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"booking/tables", views.BookingViewSet, basename="Booking")

urlpatterns = [
    path("", views.index, name="index"),
    # add following lines to urlpatterns list
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("", include(router.urls)),
    # add following line in urlpatterns list
    path("api-token-auth/", obtain_auth_token),
]
