from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import permissions

from .models import Task
from .serializer import TaskSerializer


class TaskCreateOrListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        request = self.request

        query_s = super().get_queryset()
        return query_s.filter(user=request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


task_create_or_list_view = TaskCreateOrListView().as_view()

#
# @api_view(['POST'])
# def login(request):
#     print(request.data)
#     email = request.data['email']
#     password = request.data['password']
#
#     get_user(email, password)
#
#     user = authenticate(email=email, password=password)
#     if not user:
#         return Response({'details': 'No account for these details, please create and account instead'})
#
#     token = Token.objects.get(user=user)
#     return Response({'info': 'Login successful', 'token': token[0].key}, status=status.HTTP_200_OK)
#
#
# def get_user(email, password):
#     user = User.objects.get(email=email)
#     print(user)
#
#
# @api_view(['POST'])
# def create_account(request):
#     password = request.data['password']
#     email = request.data['email']
#     first_name = request.data['first_name']
#
#     try:
#         last_name = request.data['last_name']
#     except KeyError:
#         last_name = ''
#
#     try:
#         username = request.data['username']
#     except KeyError:
#         print('camen here')
#         username = first_name + last_name
#
#     user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name,
#                                     last_name=last_name)
#
#     token = Token.objects.get_or_create(user=user)
#
#     return Response({'message': 'Account created successfully', 'username': username, "token": token[0].key},
#                     status=status.HTTP_201_CREATED)
#
#     return Response({"token": token[0].key})
