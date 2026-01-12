from .models import User
from rest_framework import serializers

"""Создаем Сериализацию для Модели User(Пользователь)"""
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User 
        fields ='__all__'
        