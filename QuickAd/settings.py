import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '%dt-g$4948_miuo#&r5chgo42m!#5s%1$_$*8l!=^^(&!3sw00'

DEBUG = True

ALLOWED_HOSTS = ["*","torca1.herokuapp.com"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'django_extensions',
    'taggit',
    'rest_framework',
    'django_filters',
    'core',
    'ads',
    'users',
    'accounts',
    'category',
    'stripe',
    'djstripe',
    'crispy_forms',
    'django_private_chat',
    'subscriptions',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    #'notifications',
    #'django_messages',
    'six',
    'social_django',
    
    #'pinax.notifications',
    #'mailer',
]  

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'djstripe.middleware.SubscriptionPaymentMiddleware',
    
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}





SITE_ID = 2

EMAIL_BACKEND = "mailer.backend.DbBackend"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ROOT_URLCONF = 'QuickAd.urls'

FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.login_redirect',
                'social_django.context_processors.backends', 
            ],
            'libraries':{
            'user_tags': 'accounts.templatetags.usertags',

            }
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
    
    'django_messages.context_processors.inbox',
)

DJANGO_MESSAGES_NOTIFY = False

WSGI_APPLICATION = 'QuickAd.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tires.sqlite'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



#private_chat

CHAT_WS_SERVER_HOST = 'localhost'
CHAT_WS_SERVER_PORT = 5002
CHAT_WS_SERVER_PROTOCOL = 'ws'

#CHAT_WS_SERVER_HOST =  '0.0.0.0'
#CHAT_WS_SERVER_PROTOCOL = 'wss'
#CHAT_WS_SERVER_PORT = int(os.environ.get('PORT', 5002))



#STRIPE_PUBLISHABLE_KEY = 'pk_test_eGMbcpswSjblf9dzmh5hhpBW00l2d07cpA'
#STRIPE_SECRET_KEY = 'sk_test_gsyDXO3WH0eB4EjCEe8w5m2600d9Q9XmXW'


#STRIPE_LIVE_PUBLIC_KEY = os.environ.get("STRIPE_LIVE_PUBLIC_KEY", "<your publishable key>")
#STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "<your secret key>")
STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_eGMbcpswSjblf9dzmh5hhpBW00l2d07cpA")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_gsyDXO3WH0eB4EjCEe8w5m2600d9Q9XmXW")
STRIPE_LIVE_MODE = False  # Change to True in production
DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint


STRIPE_API_VERSION = "2019-09-09"



AUTH_USER_MODEL = "accounts.User"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TAGGIT_CASE_INSENSITIVE = False

CORS_ORIGIN_ALLOW_ALL = True


import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 'social_core.backends.facebook.FacebookOAuth2',
 'django.contrib.auth.backends.ModelBackend',
 )

SOCIAL_AUTH_FACEBOOK_KEY = '574070036551707'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'ef9458e5df36b52e61881dda51e6d707'




