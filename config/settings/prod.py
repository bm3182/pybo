from .base import *

ALLOWED_HOSTS = ['152.70.245.135', 'bm3182.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pybo',
        'USER': 'master',
        'PASSWORD': 'P@ssw0rd',
        'HOST': 'mysql-MDS1.subnet05120955.vcn05120955.oraclevcn.com',
        'PORT': '3306',
    }
}