from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from notifier.consumers import NoseyConsumer, SentenceConsumer
from channels.http import AsgiHandler

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NoseyConsumer),
        path("sentences/", SentenceConsumer),

        # AsgiHandler is "the rest of Django" - send things here to have Django
        # views handle them.
        re_path("^", AsgiHandler),
    ]),
})
