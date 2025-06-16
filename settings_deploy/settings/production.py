from .base import *

DEBUG = False
ALLOWED_HOSTS = ['dipleey.com', 'www.dipleey.com']
CSRF_TRUSTED_ORIGINS = ['https://dipleey.com', 'https://www.dipleey.com']


try:
    from .local import *
except ImportError:
    pass
