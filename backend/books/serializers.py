from .models import Author,Genre,BookType,Book
from rest_framework import serializers


"""Создаем Сериализацию для Модели Author"""
class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author 
        # передаем атрибуты модели
        fields = [ 'id','name','year_of_birth','biography','country']
        
        
"""Создаем Сериализацию для Модели Genre"""
class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre 
        #  передаем атрибуты модели
        fields = ['id','title']
        
"""Создаем Сериализацию для Модели BookType"""
class BookTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookType
        #  передаем атрибуты модели
        fields = ['id','cover','language']
        
"""Создаем Сериализацию для Модели Book"""
class BookSerializer(serializers.ModelSerializer):
    
    """Передаем атрибуты передаются по первичному ключу"""
    # Тип книги
    book_type = BookTypeSerializer(write_only=True)
    # Автор
    author = AuthorSerializer(write_only= True)
    # Жанр
    genre = GenreSerializer(write_only= True)    
     
    class Meta:
        model = Book
        #  передаем атрибуты модели
        fields = ['id','author','genre','book_type','title']
        
        
        
        