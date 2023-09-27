from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm


def ajouter_billet(request):
    if request.method == 'POST':
        form = BilletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'liste_billets')  # Redirigez vers la liste des billets ou une autre page après la création du billet
    else:
        form = BilletForm()

    return render(request, 'ajouter_billet.html', {'form': form})
