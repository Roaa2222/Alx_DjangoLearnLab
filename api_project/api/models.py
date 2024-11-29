from django.db import models

#class Book(models.Model):
    #title = models.CharField(max_length=200)
    #author = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title
