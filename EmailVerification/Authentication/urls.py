from django.urls import path
from .views import SignUpview, LoginView, LogOutView
from .views import activate


urlpatterns = [
    path("s/", SignUpview.as_view(), name='Sign_url'),
    path('a/', LoginView.as_view(), name='login_url'),
    path('b/', LogOutView.as_view(), name='log_url'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]