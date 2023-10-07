from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserFollows

from .models import BookReviewTicket, BookReview
from .forms import BookReviewTicketForm, BookReviewForm

class HomeListView(ListView):
    template_name = "combined_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = BookReviewTicket.objects.all()
        context["reviews"] = BookReview.objects.all()
        return context

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

    return render(request, 'ticket_detail.html', {'ticket': ticket})


    return render(request, 'ticket_detail.html', {'ticket': ticket})
def book_review_detail(request, review_id):
    # Récupérer la critique (BookReview) associée à l'identifiant review_id
    review = get_object_or_404(BookReview, id=review_id)

    # Récupérer le ticket (BookReviewTicket) associé à la critique
    ticket = review.ticket

    # Vous pouvez maintenant passer review et ticket à votre template
    return render(request, 'book_review_detail.html', {'review': review, 'ticket': ticket})

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
def create_book_review(request):
    ticket_id = request.GET.get('ticket_id')
    ticket = None

    if ticket_id:
        ticket = get_object_or_404(BookReviewTicket, id=ticket_id)

    if request.method == 'POST':
        if ticket:
            ticket_form = BookReviewTicketForm(request.POST, instance=ticket)
            form = BookReviewForm(request.POST)
        else:
            ticket_form = BookReviewTicketForm(request.POST)
            form = BookReviewForm(request.POST)

        if form.is_valid() and ticket_form.is_valid():
            if not ticket:
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.save()

            review = form.save(commit=False)
            review.author = request.user
            review.ticket = ticket
            review.save()
            return redirect('ticket_list')
    else:
        if ticket:
            ticket_form = BookReviewTicketForm(instance=ticket)
        else:
            ticket_form = BookReviewTicketForm()
        form = BookReviewForm()

    return render(request, 'create_book_review.html', {'form': form, 'ticket_form': ticket_form})



@login_required
def manage_followers(request):
    if request.method == 'POST':
        # Récupérez le nom de l'utilisateur à suivre depuis le formulaire
        username_to_follow = request.POST.get('username_to_follow')
        # Recherchez l'utilisateur avec ce nom
        user_to_follow = CustomUser.objects.filter(username=username_to_follow).first()
        if user_to_follow:
            # Créez une relation de suivi entre l'utilisateur connecté et l'utilisateur cible
            UserFollows.objects.get_or_create(user=request.user, followed_user=user_to_follow)

    # Récupérez les utilisateurs suivis par l'utilisateur connecté
    following = UserFollows.objects.filter(user=request.user)
    # Récupérez les utilisateurs qui suivent l'utilisateur connecté
    followers = UserFollows.objects.filter(followed_user=request.user)

    return render(request, 'manage_followers.html', {'following': following, 'followers': followers})
