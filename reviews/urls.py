from django.urls import path
from . import views
from .views import combined_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.combined_list, name='home'),
    path('reviews/', views.book_review_list, name='book_review_list'),
    path('reviews/<int:review_id>/', views.book_review_detail, name='book_review_detail'),
    path('reviews/new/', views.create_book_review, name='create_book_review'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/new/', views.create_book_review_ticket, name='create_ticket'),
    path('combined_list/', views.combined_list, name='combined_list'),
    path('ticket-confirmation/', views.ticket_confirmation, name='ticket_confirmation'),
    path('manage_followers/', views.manage_followers, name='manage_followers'),
    path('response_review/<int:ticket_id>/', views.response_review, name='response_review'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)