from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # Indexed field
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
