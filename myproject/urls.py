from django.contrib import admin
from django.urls import path
from login import views # Importez la vue home depuis login.views
from django.contrib.auth.views import LoginView
from reviews import TicketViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),  # Utilisez la vue home depuis login.views
    path('signup/', views.signup, name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('ajouter_billet/', TicketViews.ajouter_billet, name='ajouter_billet'),
]
