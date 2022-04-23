from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),
    path('book-create', BookCreate.as_view(), name='book-create'),
    path('book-update/<int:pk>', BookUpdate.as_view(), name='book-update'),
    path('book-delete/<int:pk>', BookDelete.as_view(), name='book-delete'),
]