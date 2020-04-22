# old version of this file

import os
from channels.layers import get_channel_layer
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channelsproj.settings")
channel_layer = get_channel_layer()
django.setup()
application = get_default_application()

########################

# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channelsproj.settings")
# django.setup()
# application = get_default_application()
