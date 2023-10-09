from django.contrib import admin
from .models import BookReview, BookReviewTicket

# Register your models here.
admin.site.register(BookReview)
admin.site.register(BookReviewTicket)
