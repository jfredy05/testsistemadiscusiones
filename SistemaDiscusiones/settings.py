# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os --> eliminar por unipath
from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zc8ez5u0#ixe3cul1_p8pbd=7ac*k7_4-(je&kxcy7$mf6i4c@'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER': 'cursodjango',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '1715',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'social.apps.django_app.default',
    'djrill',
    'apps.home',
    'apps.discuss',
    # 'apps.users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SistemaDiscusiones.urls'

WSGI_APPLICATION = 'SistemaDiscusiones.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = ''

# AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
        'social.backends.facebook.FacebookAppOAuth2',
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.twitter.TwitterOAuth',
        'django.contrib.auth.backends.ModelBackend',
    )

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/error/'

# SOCIAL_AUTH_USER_MODEL = 'users.User'

SOCIAL_AUTH_FACEBOOK_KEY = '1688928988041572'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd492b87faa582ca3cde36db52f1201f8'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = 'kAjDTVTIMg3HPCpx0jPOmK4zz'
SOCIAL_AUTH_TWITTER_SECRET = 'h9icF7GiqttJi1BulrsECjUjwv70PWsHfWY650A9pUw0xGEqHZ'

SOCIAL_AUTH_PIPELINE = (
        'social.pipeline.social_auth.social_details',
        'social.pipeline.social_auth.social_uid',
        'social.pipeline.social_auth.auth_allowed',
        'social.pipeline.social_auth.social_user',
        'social.pipeline.user.get_username',
        'social.pipeline.user.create_user',
        'social.pipeline.social_auth.associate_user',
        'social.pipeline.social_auth.load_extra_data',
        'social.pipeline.user.user_details',
        'apps.users.pipelines.get_avatar',
    )

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = 'ac65dc8305a1d4146de45c281bbc1242-us7'