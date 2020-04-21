from django import forms
from .models import Book, Sentence

class BookForm(forms.ModelForm):
    book_title = 'Book'

    class Meta:
        model = Book
        fields = ('title',)


class SentenceForm(forms.ModelForm):
    book_title = 'Sentence'

    class Meta:
        model = Sentence
        fields = ('sentence',)
