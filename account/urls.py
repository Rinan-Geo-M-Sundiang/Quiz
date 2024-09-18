from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),  # Home will redirect to view_profile
    path('register/', register, name='register'),
    path('create_profile/', profile_creation, name='create_profile'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/', view_profile, name='view_profile'),
    path('login/', user_login, name='login'),  # Main login URL
    path('accounts/login/', user_login, name='accounts_login'),  # Optional additional login URL
]
