from django.shortcuts import render, redirect, get_object_or_404
from .models import BookReviewTicket, BookReview
from .forms import BookReviewTicketForm
from .forms import BookReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def list_book_review_tickets(request):
    tickets = BookReviewTicket.objects.all()
    return render(request, 'list_tickets.html', {'tickets': tickets})

def ticket_list(request):
    # Retrieve all ticket objects
    tickets = BookReviewTicket.objects.all()

    return render(request, 'ticket_list.html', {'tickets': tickets})
def book_review_list(request):
    # Query for all book reviews
    book_reviews = BookReview.objects.all()

    return render(request, 'combined_list.html', {'book_reviews': book_reviews})
def combined_list(request):
    tickets = BookReviewTicket.objects.all()
    reviews = BookReview.objects.all()
    return render(request, 'combined_list.html', {'tickets': tickets, 'reviews': reviews})

def ticket_detail(request, ticket_id):
    # Retrieve the book review ticket object or return a 404 error if it doesn't exist
    ticket = get_object_or_404(BookReviewTicket, pk=ticket_id)

    return render(request, 'book_review_ticket_detail.html', {'ticket': ticket})


    return render(request, 'ticket_detail.html', {'ticket': ticket})
def book_review_detail(request, pk):
    # Retrieve the specific book review using the primary key (pk)
    book_review = get_object_or_404(BookReview, pk=pk)

    return render(request, 'book_review_detail.html', {'book_review': book_review})

@login_required
def create_book_review_ticket(request):
    if request.method == 'POST':
        form = BookReviewTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Associate the ticket with the logged-in user
            ticket.save()
            return redirect('ticket_confirmation')
    else:
        form = BookReviewTicketForm()

    return render(request, 'create_ticket.html', {'form': form})


def ticket_confirmation(request):
    return render(request, 'ticket_confirmation.html')
@login_required
def create_book_review(request, ticket_id):
    ticket = BookReviewTicket.objects.get(pk=ticket_id)

    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.ticket = ticket
            review.save()
            return redirect('ticket_detail', ticket_id=ticket.id)

    else:
        form = BookReviewForm()

    return render(request, 'create_book_review.html', {'form': form, 'ticket': ticket})