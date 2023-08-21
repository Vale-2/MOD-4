from django.urls import path
from .views import index, top_sellers, register, advertisement_post

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name = 'register'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('advertisement_post/', advertisement_post, name = 'advertisement_post'),
#    path('login_post', login_post, name = 'login_post'),
#    path('profile/', profile, name = 'profile'),
]
