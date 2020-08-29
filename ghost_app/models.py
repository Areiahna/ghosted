from django.db import models
from django.utils import timezone


# Create your models here.


class PostModel (models.Model):

    POST_CHOICES = (
        ("Roast", "Roast"),
        ("Boast", "Boast")
    )
    post = models.CharField(max_length=20, choices=POST_CHOICES)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    text = models.CharField(max_length=150)
    post_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.text

    def vote_score(self):
        return self.upvotes - self.downvotes
