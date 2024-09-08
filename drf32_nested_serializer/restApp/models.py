from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=90)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.book_name