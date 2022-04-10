from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import permissions

from .models import Task
from .serializer import TaskSerializer


class TaskCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        request = self.request
        query_s = super().get_queryset()
        return query_s.filter(user=request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


task_create_or_list_view = TaskCreateView().as_view()


@api_view(['POST'])
def login(request, ):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)
    if not user:
        user = User.objects.create_user(username=username, password=password)
    print(Token.objects.all())
    token = Token.objects.get_or_create(user=user)

    return Response({"token": token[0].key})
