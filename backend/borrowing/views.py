from .models import BookCopy,Borrowing
from .serializers import BookCopySerializer,BorrowingSerializer
from rest_framework import viewsets


"""Создаем Представление для Модели BookCopy"""
class BookCopyViewSet(viewsets.ModelViewSet):
    
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    
     
    
"""Создаем Представление для Модели Borrowing"""  
class BorrowingViewSet(viewsets.ModelViewSet):
    
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    