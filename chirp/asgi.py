"""
ASGI config for chirp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chirp.settings')

# application = get_asgi_application()

import os

from django.core.asgi import get_asgi_application


# chanels
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import home.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chirp.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': URLRouter(
        home.routing.websocket_urlpatterns
    )
})
