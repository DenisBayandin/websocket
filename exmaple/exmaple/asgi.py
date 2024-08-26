"""
ASGI config for exmaple project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from websocket.consumer import CustomConsumer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exmaple.settings")
application = ProtocolTypeRouter({  # определяем, какие типы протоколов обрабатываются
    "http": get_asgi_application(),  # стандартное ASGI-приложение для обработки HTTP
    "websocket": URLRouter([  # обработка WebSocket запросов
            path("ws/note/", CustomConsumer.as_asgi()),  # привязываем определенного consumer-а (к примеру: разная логика)
        ])
})
