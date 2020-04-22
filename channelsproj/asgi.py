import os
import django
from channels.routing import application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channelsproj.settings")
django.setup()
application = application()
