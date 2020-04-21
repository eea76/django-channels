from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifier.models import Book, Sentence
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=Book)
def announce_new_book(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "book.gossip",
                       "event": "New Book",
                       "book_name": instance.title,
                       "book_id": instance.id,
                       "player_name": instance.player_name.id})


@receiver(post_save, sender=Sentence)
def announce_new_sentence(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        print(instance.sentence)

        async_to_sync(channel_layer.group_send)(
            "announcement", {"type": "sentence.announcement",
                       "event": "New Sentence",
                       "sentence_name": instance.sentence,
                       "sentence_id": instance.id,
                       "submitter": instance.submitter.id})
