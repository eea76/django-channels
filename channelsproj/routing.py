from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifier.consumers import NoseyConsumer, SentenceConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NoseyConsumer),
        path("sentences/", SentenceConsumer),
    ])
})
