from django.urls import path,include
from .views import register,user_login,user_home,user_logout

urlpatterns = [
    path('',user_home,name='home'),
    path('login/',user_login,name='login'),
    path('register/',register,name='register'),
    path('logot/',user_logout,name='logout')
]