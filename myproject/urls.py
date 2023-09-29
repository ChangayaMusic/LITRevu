from django.contrib import admin
from django.urls import path
from login import views # Importez la vue home depuis login.views
from django.contrib.auth.views import LoginView
from reviews import TicketViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('reviews/', TicketViews.book_review_list, name='book_review_list'),
    path('reviews/<int:review_id>/', TicketViews.book_review_detail, name='book_review_detail'),
    path('reviews/new/', TicketViews.create_book_review, name='create_book_review'),
    path('tickets/', TicketViews.ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', TicketViews.ticket_detail, name='ticket_detail'),
    path('tickets/new/', TicketViews.create_book_review_ticket, name='create_ticket'),
    path('combined_list/', TicketViews.combined_list, name='combined_list'),
    path('ticket-confirmation/', TicketViews.ticket_confirmation, name='ticket_confirmation'),
]
