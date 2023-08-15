from django.urls import path
from .views import registerUsers,loginUser,logoutUser,resetPass



app_name="users"
urlpatterns = [
    path("register/",registerUsers,name="signup"),
    path("login/",loginUser,name="login"),
    path("logout/",logoutUser,name="logout"),
    path("resetPassword/",resetPass,name="reset")
]