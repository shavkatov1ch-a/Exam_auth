from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.request import Request
from django.contrib.auth import authenticate, login, logout
from .tokens import create_jwt_pair_for_user
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import SignUpSerializer


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                 'message': 'User created successfully',
                 'data': serializer.data
             }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                'message': 'Login successfully',
                'token': tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request, *args, **kwargs):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)