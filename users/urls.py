from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.UserList.as_view()),
    path('get-message/', views.getMessage),
    path('add-message/', views.addMessage),

]
