from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate

urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),
    path('book-create', BookCreate.as_view(), name='book-create'),
    path('book-update/<int:pk>', BookUpdate.as_view(), name='book-update'),
]