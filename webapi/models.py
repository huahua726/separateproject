from django.db import models


# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=64)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'
