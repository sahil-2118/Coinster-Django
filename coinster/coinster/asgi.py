"""
ASGI config for coinster project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinster.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from scheduler.consumers import SchedulerConsumer
from scheduler.middlewares import TokenAuthMiddleWare
from django.urls import path,re_path




application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": 
        AllowedHostsOriginValidator(
            TokenAuthMiddleWare(
            URLRouter([path('v1/scheduler/', SchedulerConsumer.as_asgi())])
        )
    ),
})
