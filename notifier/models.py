from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    genre_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.genre_name


class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    publication_date = models.CharField(max_length=20, null=True)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.CASCADE)
    player_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    was_guessed_correctly = models.BooleanField(default=False)
    already_played = models.BooleanField(null=True, default=False)

    def __str__(self):
        return str(self.title)



class Sentence(models.Model):
    sentence = models.CharField(max_length=400, null=True, blank=True)
    vote_count = models.IntegerField(default=0, null=True, blank=True)
    is_real = models.BooleanField(default=False)
    is_winner = models.BooleanField(default=False)
    submitter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    guessed_by = models.ManyToManyField('auth.User', related_name="sentence_guessed_by", null=True, blank=True)

    def __str__(self):
        return str(self.sentence) + ' - ' + str(self.submitter)


class UserSentence(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    guessed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + ' ' + str(self.book)
