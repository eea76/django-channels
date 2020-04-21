from django.shortcuts import render, redirect

from notifier.models import *

from .forms import BookForm, SentenceForm

def index(request):
    users = User.objects.all()
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.player_name = request.user
            book.save()
            return redirect('/')
    else:
        form = BookForm()

    obj = {
        'users' : users,
        'books' : books,
        'form' : form,
    }

    return render(request, 'home.html', obj)


def book_detail(request, id):
    book = Book.objects.get(id=id)
    sentences = Sentence.objects.filter(book_name=book.id)

    if request.method == 'POST':
        form = SentenceForm(request.POST)
        if form.is_valid():
            sentence = form.save(commit=False)
            sentence.submitter = request.user
            sentence.book_name = book
            sentence.save()
            return redirect('/book/' + str(book.id))
    else:
        form = SentenceForm()

    obj = {
        'book': book,
        'sentences': sentences,
        'form': form,
    }

    return render(request, 'book_detail.html', obj)
