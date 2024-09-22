from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs)->Response:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def put(self,request, *args, **kwargs)->Response:
        serializer = self.get_serializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class RegisterView(APIView):
    """ 
    Registering a user
    """
    
    def post(self,request)->Response:

        data = request.data
        if not all(token in data for token in ['username', 'email', 'password']):
            return Response({'message': 'Some data is missing'}, status = 400)
        
        try:
            # Creating user
            user = User.objects.create_user(username=data['username'], email = data['email'], password = data['password'])
            user.save()
            return Response({'message': 'User created successfully'}, status = 201)
        except Exception as e:
            return Response({'message': f'Error because {str(e)}'}, status = 400)
        
class LoginView(APIView):
    def post(self,request)->Response:
        data = request.data
        if not all(token in data for token in ['username', 'password']):
            return Response({'message': 'Some data is missing'}, status = 400)
        
        try:
            user = User.objects.get(username = data['username'])
            
            if user.check_password(data['password']):
                refresh = RefreshToken.for_user(user)   

                #Refreshing token
                return Response({
                    'message': 'User logged in successfully',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=201)
            else:
                return Response({'message': 'Invalid Credentials'}, status = 400)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status = 400)
        except Exception as e:
            return Response({'message': f'Error because {str(e)}'}, status = 400)