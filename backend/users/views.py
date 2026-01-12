from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets


"""Создаем Представление для Модели User(Пользователь)"""
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
