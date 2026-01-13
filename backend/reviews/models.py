from django.db import models
from users.models import User



"""Создаем Модель Reviews (отзывы)"""
class Reviews(models.Model):
    
    """Передаем автора отзыва по первичному ключу """
    review_author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # текст отзыва
    text = models.CharField(max_length=250)
    
    # оценка
    estimation = models.CharField(max_length=20,choices=[
        ('One star','одна звезда'),
        ('Two','две звезды'),
        ('Three stars','три звезды'),
        ('Four stars','четыре звезды'),
        ('Five stars','пять звезд'),
        
    ])
    
    """Передаем магический метод str"""
    def __str__(self) -> str:
        return self.text