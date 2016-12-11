import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iv5%rh+iwj1)&hv015rp#*&q+llqg52zihv$#ino%7x@)u!$20'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    
    'import_export',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'perfil',
    # mi app antes pa el logout
    'django.contrib.admin',
    # Social Auth
    'social.apps.django_app.default',
    'eventos',
    'mailin',
    'main',
    'markdown_deux',
    'pagos',
    #Aplicaciones
    'applys',


    ]


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Excepcion cuando cancelan el login 
    # 'perfil.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'geek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Agrego esto para la carpeta media
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'geek.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases



# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
# if not DEBUG:
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME':'geek',
            'USER':'admin',
            'PASSWORD':'Poweroso77',
            # 'HOST':'54.213.147.140',
            # 'HOST':'54.200.214.156',
            'HOST':'localhost',
            # 'PORT':'5432',
            'PORT':''
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR,"static"),)
# STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')


LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

# Backend authentication propio FIXTER
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'account.authentication.EmailAuthBackend',
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth2',

    )
SOCIAL_AUTH_FACEBOOK_KEY='421914394679473'#Facebook app ID
SOCIAL_AUTH_FACEBOOK_SECRET='64351e9c281191cf774af476479a566a'# Facebook App secret
SOCIAL_AUTH_FACEBOOK_SCOPE=['email',]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email, age_range'
}

SOCIAL_AUTH_TWITTER_KEY = 'Qyzcr8N3UJgQgQpFeXaiVKxXp' #consumer key
SOCIAL_AUTH_TWITTER_SECRET = '9uLpRrVdIA5NX9c5rEjg7mkjVGRIbkqJSfy2H7TfGxQe00gpGS' #Consumer secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '773946138609-lrt0vme6hr6kbqgavvaerov44pcu9mo8.apps.googleusercontent.com' #Google consumer key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '-5iamsoiKaBnlZWZ3kp1ArHF' #secret


# Correo electronico
EMAIL_HOST = 'p3plcpnl0061.prod.phx3.secureserver.net'
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT = '587'
EMAIL_PORT='465'
EMAIL_HOST_USER = 'admin@fixter.org'
# EMAIL_HOST_USER = 'tterrenofacil@gmail.com'
EMAIL_HOST_PASSWORD = 'Poweroso77'
# EMAIL_HOST_PASSWORD = 'Miguel741010'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL=False

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'perfil.pipelines.save_profile_picture',  # <--- set the import-path to the function
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

# BROKER_HOST = "localhost"
# BROKER_PORT = 5672
# BROKER_USER = "root"
# BROKER_PASSWORD = "root"
# BROKER_VHOST = "localhost"

# BROKER_URL = "amqp://guest:guest@localhost:5672//"

# CELERY_RESULT_BACKEND = "amqp"

BROKER_URL = 'amqp://bliss:poweroso@localhost:5672//'

# LOGIN_ERROR_URL = reverse_lazy('login')
# SOCIAL_AUTH_LOGIN_ERROR_URL = reverse_lazy('main:home')

