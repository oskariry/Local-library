from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # Genres and books that contains input word
    input_text = request.GET.get('input_text')
    num_books_contains = Book.objects.all()
    num_genres_contains = Genre.objects.all()
    if input_text != '' and input_text is not None:
        num_books_contains = num_books_contains.filter(title__icontains=input_text).count()
        num_genres_contains = num_genres_contains.filter(name__icontains=input_text).count()

    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_contains': num_books_contains,
        'num_genres_contains':  num_genres_contains,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model = Book
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
class AuthorDetailView(generic.DetailView):
    model = Author
