"""
WSGI config for myfirstproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# WSGI (Web Server Gateway Interface)
# - 웹 서버와 장고 어플리케이션을 연결하는 표준 인터페이스
# - 동기 방식의 서버 환경에서 사용됨

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')

application = get_wsgi_application()
