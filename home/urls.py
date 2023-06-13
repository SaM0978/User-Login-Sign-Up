from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard")
]