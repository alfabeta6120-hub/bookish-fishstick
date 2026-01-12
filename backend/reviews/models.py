from django.db import models
from users.models import User



"""Создаем Модель Reviews (отзывы)"""
class Reviews(models.Model):
    
    """Передаем автора отзыва по первичному ключу """
    review_author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # текст отзыва
    text = models.TextField(blank=True)
    
    # оценка
    estimation = models.CharField(max_length=20,choices=[
        ('good','хорошо'),
        ('excellent','отлично'),
        ('badly','плохо'),
        
    ])
    
    """Передаем магический метод str"""
    def __str__(self) -> str:
        return self.text