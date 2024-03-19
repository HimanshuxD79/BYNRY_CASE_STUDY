from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.register, name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/', views.user_logout, name='logout'),

]