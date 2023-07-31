from django.urls import path
from .views import UserSignupView, UserSigninView, UserSignoutView

urlpatterns = [
    # 사용자
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserSigninView.as_view(), name='login'),
    path('logout/', UserSignoutView.as_view(), name='logout'),
]