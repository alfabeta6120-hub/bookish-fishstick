from .models import Reviews
from rest_framework import serializers
from users.serializers import UserSerializer


"""Создаем Сериализацию для Модели Reviews(отзывы)"""
class ReviewsSerializer(serializers.ModelSerializer):
    
    # отзывы пользователя
    review_author = UserSerializer(read_only=True)
    
    class Meta:
        model = Reviews
         #  передаем атрибуты модели 
        fields = ['id','review_author','text','estimation']