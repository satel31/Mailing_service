from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.users.views import RegisterView,ActivationView, ProfileView

app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/activation/', ActivationView.as_view(), name='activation'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
]