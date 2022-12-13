from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User, Message

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .serializers import UserSerializer, MessageSerializer
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
@api_view(['GET'])
def getMessage(request):
    message = Message.objects.all()
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)

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



@api_view(['POST'])
def addMessage(request):
    # message = Message.objects.all()
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from rest_framework import generics, permissions
# from .models import Message
# from .serializers import MessageSerializer

# class MessageList(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     def perform_create(self, serializer):
#         recipient = get_object_or_404(User, username=self.request.data['recipient'])
#         serializer.save(sender=self.request.user, recipient=recipient)

# class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


