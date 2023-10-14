from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserFollows
from django.views.generic import ListView
from operator import attrgetter
from .models import BookReviewTicket, BookReview
from .forms import BookReviewTicketForm, BookReviewForm


import itertools


class HomeListView(ListView):
    template_name = "combined_list.html"

    def get_queryset(self):
        # Vous pouvez personnaliser la logique ici pour récupérer les tickets et les critiques que vous souhaitez afficher.
        queryset = chain(BookReviewTicket.objects.all(), BookReview.objects.all())

        # Utilisez print pour afficher le contenu du queryset (à des fins de débogage)
        for item in queryset:
            print(item)  # Vous pouvez personnaliser cette sortie pour afficher les données pertinentes

        return queryset

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
    # Récupérez tous les tickets et les critiques
    tickets = list(BookReviewTicket.objects.all())
    reviews = list(BookReview.objects.all())

    # Fusionnez les deux listes en une seule
    combined_list = tickets + reviews

    # Triez la liste combinée par date
    combined_list.sort(key=lambda item: item.date, reverse=True)

    context = {
        'combined_list': combined_list,
    }
    return render(request, 'combined_list.html', context)

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

def response_review(request, ticket_id):
    # Récupérer l'objet Ticket en fonction de l'ID
    ticket = get_object_or_404(BookReviewTicket, pk=ticket_id)

    if request.method == 'POST':
        # Si le formulaire est soumis, traiter les données du formulaire
        form = BookReviewForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide, enregistrez la critique associée au ticket
            review = form.save(commit=False)
            review.author = request.user  # Vous devrez peut-être ajuster cela en fonction de la manière dont vous gérez les auteurs
            review.ticket = ticket
            review.save()

            # Enregistrez le message flash de succès
            messages.success(request, 'Votre critique a été enregistrée avec succès.')

            # Redirigez l'utilisateur vers une page de confirmation ou ailleurs
            return redirect('ticket_detail', ticket_id=ticket_id)
    else:
        # Si c'est une requête GET, affichez le formulaire vide
        form = BookReviewForm()

    # Affichez la page de réponse avec le formulaire
    return render(request, 'response_review.html', {'form': form, 'ticket': ticket})


def user_reviews_tickets(request):
    # Récupérez les tickets et les critiques de l'utilisateur connecté
    user_reviews = BookReview.objects.filter(author=request.user)
    user_tickets = BookReviewTicket.objects.filter(user=request.user)

    return render(request, 'user_reviews_tickets.html', {
        'user_reviews': user_reviews,
        'user_tickets': user_tickets,
    })

def modify_review(request, review_id):
    review = get_object_or_404(BookReview, id=review_id)

    if request.method == 'POST':
        form = BookReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('combined_list')  # Redirigez l'utilisateur vers la liste combinée après la modification

    else:
        form = BookReviewForm(instance=review)

    return render(request, 'modify_review.html', {'form': form, 'review': review})


def modify_ticket(request, ticket_id):
    ticket = get_object_or_404(BookReviewTicket, id=ticket_id)

    if request.method == 'POST':
        form = BookReviewTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('user_reviews_tickets')  # Redirigez l'utilisateur vers la liste combinée après la modification

    else:
        form = BookReviewTicketForm(instance=ticket)

    return render(request, 'modify_ticket.html', {'form': form, 'ticket': ticket})