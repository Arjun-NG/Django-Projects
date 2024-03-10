from django.urls import path,include
from blog import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('login/',views.loginn,name="login"),
    path('signup/',views.signup,name="signup"),
    path("newpost/",views.newpost,name="newpost"),
    path("mypost/",views.mypost,name="mypost"),
    path("signout/",views.signout,name="signout"),
    
]