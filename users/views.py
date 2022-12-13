from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        if(User.objects.filter(username=username, password=password).exists):
            # login(request, username)
            # return render(request, 'users/home.html')
            return HttpResponse(status=200)
        else:
            # return render(request, 'users/login.html', {'error': 'Invalid username or password'})
            return HttpResponse(status=401)

    else:
        return HttpResponse(status=405)
    #     return render(request, 'users/login.html')


from .serializers import UserSerializer
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
