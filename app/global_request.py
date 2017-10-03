from threading import local
from django.utils.deprecation import MiddlewareMixin


_global = local()


def get_current_request():
    """requestを取り出す"""
    return getattr(_global, 'request')


class GlobalRequestMiddleware(MiddlewareMixin):
    """requestを保存しておくミドルウェア"""

    def process_request(self, request):
        _global.request = request
        return self.get_response(request)
