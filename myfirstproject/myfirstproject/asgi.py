"""
ASGI config for myfirstproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# ASGI (Asynchronous Server Gateway Interface)
# - 비동기 처리를 지원
# - 실시간 기능 (채팅, 알림, 웹소켓 등)을 구현할 때 사용

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')

application = get_asgi_application()
