from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('author.Author', on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField(max_length=200, help_text='Enter a description of the book')
    #genre = models.ManyToManyField(Genre)
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    #image = models.ImageField(upload_to="books/", blank=True, default="book-placeholder.jpeg")
