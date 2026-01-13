from users.serializers import UserSerializer
from books.serializers import BookSerializer
from .models import BookCopy,Borrowing
from rest_framework import serializers

"""Создаем Сериализацию для Модели BookCopy(экземпляр книги)"""
class BookCopySerializer(serializers.ModelSerializer):
    
    # книга
    book = BookSerializer(read_only=True)
    
    class Meta:
        model = BookCopy
        #  передаем атрибуты модели
        fields = ['id','book','status','quantity']
        
        

"""Создаем Сериализацию для Модели Borrowing (Выдача книг)"""
class BorrowingSerializer(serializers.ModelSerializer):
    
    # экземпляр книги
    book_copy = BookCopySerializer(read_only=True)
    # пользователь
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Borrowing
         #  передаем атрибуты модели
        fields = ['id','booking','date_of_issue','deadline','forfeit','book_copy','user']