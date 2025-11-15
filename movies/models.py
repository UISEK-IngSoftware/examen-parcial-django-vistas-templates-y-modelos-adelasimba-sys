from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director_name = models.CharField(max_length=150)
    year_published = models.PositiveIntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.year_published})"