#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 명령어 실행 (ex. runserver, startapp 등)
    execute_from_command_line(sys.argv)

# 현재 파일(모듈)이 직접 실행될 때 main() 함수 실행
# * 직접 실행 예시 : python manage.py runserver
# * 세번째 인자 'runserver' 와 같은 옵션 없이 실행하면
#   사용 가능한 명령어 목록이 출력됨!
if __name__ == '__main__':
    main()
