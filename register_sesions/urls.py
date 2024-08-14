from django.urls import path
from .views import login_view, logout_view, save_player

urlpatterns = [
    path('', login_view, name='login'),
    path('save_player/', save_player, name='save_player'),
    path('logout/', logout_view, name='logout'),
]
