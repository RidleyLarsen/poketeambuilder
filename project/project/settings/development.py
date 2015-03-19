'''
    Local Development Settings
'''

from base import *

DEBUG = True

SECRET_KEY = 'pc0e!i9-t#t2=xdvl7n@2c&m)ho-3jai8er8&$a_0noa4yos8c'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': '10.0.0.254',
        'PORT': '',
    }
}
