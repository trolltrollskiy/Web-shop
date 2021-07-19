from django.urls import path
from .views import CreateUserAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = 'users'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', CreateUserAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view())
]
