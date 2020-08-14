from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mhsp1948$default",
        'USER': "mhsp1948",
        'PASSWORD': os.getenv("DB_PASS"),
        'HOST': "mhsp1948.mysql.pythonanywhere-services.com",
    }
}

ALLOWED_HOSTS = ['www.mikehprice.com']

SECRET_KEY = os.getenv("SECRET_KEY")

try:
    from .local import *
except ImportError:
    pass