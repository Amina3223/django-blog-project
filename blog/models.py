"""
Models de l'aplicació blog.
"""

from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)]
    )

    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    tag = models.CharField(
        max_length=30,
        unique=True
    )

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    )

    excerpt = models.CharField(max_length=255)

    image_name = models.CharField(max_length=100)

    date = models.DateField()

    content = models.TextField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title