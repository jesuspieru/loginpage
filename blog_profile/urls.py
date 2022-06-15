from django.urls import path
from .views import ChangePasswordView
from . import views

urlpatterns = [
    path('edit-profile/', views.profile, name='edit-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]

