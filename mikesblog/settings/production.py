from .base import *

<<<<<<< HEAD
DEBUG = False

ALLOWED_HOSTS = ['*'] 
=======
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
>>>>>>> 560e78575d8a32f3c0e0eed494cb56a1b7a79033

try:
    from .local import *
except ImportError:
<<<<<<< HEAD
    pass
=======
    pass
>>>>>>> 560e78575d8a32f3c0e0eed494cb56a1b7a79033
