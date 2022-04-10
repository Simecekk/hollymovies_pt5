from django.urls import path

from books.views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
]
