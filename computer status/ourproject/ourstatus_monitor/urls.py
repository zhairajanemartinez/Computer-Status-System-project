from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for the root path
    path('use/<int:computer_id>/auth/', views.use_computer_auth, name='use_computer_auth'),
    path('book/<int:computer_id>/', views.book_computer, name='book_computer'),
    path('login/', views.login_view, name='login'),
]