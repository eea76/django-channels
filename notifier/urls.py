from django.urls import path, include

from notifier import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/<int:id>', views.book_detail, name="book_detail"),
    path('signup/', views.signup, name="signup"),
]
