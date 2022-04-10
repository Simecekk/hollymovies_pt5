from django.views.generic import ListView

from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books.html'
    extra_context = {'page_name': 'Books'}

