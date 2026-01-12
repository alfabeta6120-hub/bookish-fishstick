from django.db import models


"""Создаем Модель User (пользователь)"""
class User(models.Model):
    
    """Передаем стандартные атрибуты"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    # адрес почты
    email = models.EmailField()
    
    # телефон
    phone = models.CharField(max_length=12)
    
    """Передаем магический метод str"""
    def __str__(self) -> str:
        return self.first_name