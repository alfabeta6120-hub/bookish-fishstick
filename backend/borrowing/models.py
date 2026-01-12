from django.db import models
from books.models import Book
from users.models import User


"""Создаем Модель BookCopy (экземпляр книги)"""
class BookCopy(models.Model):
    
    # Инвентарный номер книги
    inventory_number = models.PositiveIntegerField()
    
    # Статус книги
    status = models.CharField(max_length=20,choices=[
        ('available','доступна'),
        ('issued','выдана'),
        ('repaired','ремонт')
    ])
    # Количество книг
    quantity = models.CharField(max_length=5)
    
    """Передаем атрибут по первичному ключу"""
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    
    
    """Передаем магический метод str"""
    def __str__(self) -> str:
        return self.quantity
    
       
"""Создаем Модель Borrowing (выдача книги)"""
class Borrowing(models.Model):
    
    # бронирование книг
    booking = models.CharField(max_length=20,choices=[
        ('Three days','три дня'),
        ('seven days','семь дней'),
    ])
        
    # Дата выдачи книги
    date_of_issue = models.DateTimeField(auto_now=True)
    
    # Срок сдачи книги
    deadline = models.DateTimeField(auto_now=True)
    
    # Штраф
    forfeit = models.PositiveIntegerField()
    
    """Передаем Модели по первичному ключу"""
    # тип книги
    book_copy = models.ForeignKey(BookCopy,on_delete=models.CASCADE) 
    # пользователь  
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    """Передаем магический метод str"""
    def __str__(self) -> str:
        return self.booking
    
