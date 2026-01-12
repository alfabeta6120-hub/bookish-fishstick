from .models import Author,Genre,BookType,Book
from .serializers import AuthorSerializer,GenreSerializer,BookTypeSerializer,BookSerializer
from rest_framework import viewsets


"""Создаем Представление для Модели Author(Автор)"""
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    

"""Создаем Представление для Модели Genre(Жанр)"""
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
"""Создаем Представление для Модели BookType(Тип книги)"""
class BookTypeViewSet(viewsets.ModelViewSet):
    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializer
    
    
"""Создаем Представление для Модели Book(Книга)"""
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
       
