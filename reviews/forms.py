from django import forms
from .models import BookReviewTicket
from .models import BookReview

class BookReviewTicketForm(forms.ModelForm):
    class Meta:
        model = BookReviewTicket
        fields = ['book_title', 'book_author', 'text', 'book_image']

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['title', 'rating', 'text']

