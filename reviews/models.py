from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from login.models import CustomUser
import os

def book_image_path(instance, filename):
    # Obtenez le nom du fichier d'origine
    original_filename = filename

    # Obtenez le titre du livre de l'instance
    book_title = instance.book_title

    # Générez le nouveau nom de fichier en utilisant le titre du livre et l'extension d'origine
    new_filename = f"{book_title}.{original_filename.split('.')[-1]}"

    # Retournez le chemin complet du fichier
    return os.path.join('book_images', new_filename)

class BookReviewTicket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='review_tickets')
    date = models.DateTimeField(auto_now_add=True)
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    text = models.TextField()
    book_image = models.ImageField(upload_to=book_image_path)

    def __str__(self):
        return self.book_title

class BookReview(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    text = models.TextField()
    ticket = models.ForeignKey(BookReviewTicket, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='following')
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='followers')

    class Meta:
        unique_together = ('user', 'followed_user', )

    def __str__(self):
        return f"{self.user.username} follows {self.followed_user.username}"
