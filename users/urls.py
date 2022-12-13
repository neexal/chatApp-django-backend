from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.UserList.as_view())

]
