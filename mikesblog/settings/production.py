from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*'] 

SECRET_KEY = os.getenv('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass
