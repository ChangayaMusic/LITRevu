from django.urls import path
from .views import signup, MyLogoutView, LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
