from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),
]