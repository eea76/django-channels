from django.contrib import admin

from notifier.models import *

admin.site.register(Book)
admin.site.register(Sentence)
admin.site.register(UserSentence)
