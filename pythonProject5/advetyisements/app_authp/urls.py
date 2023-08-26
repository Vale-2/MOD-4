from django.urls import path
from .views import login_view, profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]
