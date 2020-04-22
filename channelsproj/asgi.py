# old version of this file

# import os
# import channels.asgi

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat.settings")
# channel_layer = channels.asgi.get_channel_layer()

########################

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channelsproj.settings")
django.setup()
application = get_default_application()
