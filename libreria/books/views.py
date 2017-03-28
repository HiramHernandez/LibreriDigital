from django.shortcuts import render
from .models import Book
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render (request, 'books/index.html')


def listado(request):
    libros = Book.objects.all()
    return render(request, 'books/listado.html', {'books' : libros})


def detalleLibro(request, id):
    libro = get_object_or_404(Book, pk=id)
    detalle = Book.objects.filter(id=id)
    return render(request, 'books/detalle.html', {'book' : libro})


def detail(request, slug):
    #print('%s' % (slug))
    book = Book.objects.get(slug=slug)
    return render(request, 'books/detail.html', {'book':book})


