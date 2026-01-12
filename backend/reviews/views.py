from .models import Reviews
from .serializers import ReviewsSerializer
from rest_framework import viewsets


"""Создаем Представление для Модели Reviews(отзывы)"""
class ReviewsViewSet(viewsets.ModelViewSet):
    
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    
    