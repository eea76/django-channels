from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from notifier.models import *
from django.contrib.auth import login, authenticate

from .forms import BookForm, SentenceForm

def index(request):
    users = User.objects.all()
    books = Book.objects.all().order_by('-id')

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
    user_sentence = UserSentence.objects.get_or_create(book=book, user=request.user)
    already_guessed = user_sentence[0].guessed

    if request.method == 'POST':
        form = SentenceForm(request.POST)
        if form.is_valid():
            sentence = form.save(commit=False)
            sentence.submitter = request.user
            sentence.book_name = book

            user_sentence[0].guessed = True

            if book.player_name == sentence.submitter:
                sentence.is_real = True
            else:
                sentence.is_real = False

            sentence.save()
            user_sentence[0].save()
            return redirect('/book/' + str(book.id))
    else:
        form = SentenceForm()

    obj = {
        'book': book,
        'sentences': sentences,
        'form': form,
        'already_guessed': already_guessed
    }

    return render(request, 'book_detail.html', obj)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    obj = {
        'form' : form,
    }

    return render(request, 'registration/signup.html', obj)
