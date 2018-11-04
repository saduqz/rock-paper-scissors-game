import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rock_paper_scissors_game.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rock_paper_scissors_game.wsgi.application'

# Forgive me for this if
if os.environ.get("ENVIRONMENT_NAME") in ("PRODUCTION",):
    SECRET_KEY = os.environ["ROCK_PAPER_SCISSORS_SECRET_KEY"]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    DEBUG = False

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': os.environ['ROCK_PAPER_SCISSORS_DB_ENGINE'],
            'NAME': os.environ["ROCK_PAPER_SCISSORS_DB_NAME"],
            'HOST': os.environ["ROCK_PAPER_SCISSORS_DB_HOST"],
            'PORT': os.environ["ROCK_PAPER_SCISSORS_DB_PORT"],
            'USER': os.environ["ROCK_PAPER_SCISSORS_DB_USER"],
            'PASSWORD': os.environ["ROCK_PAPER_SCISSORS_DB_PASSWORD"],
        }
    }

else:
    from .local_info import NAME, HOST, PORT, USER, PASSWORD, ENGINE, SECRET_KEY

    DEBUG = True
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': ENGINE,
            'NAME': NAME,
            'HOST': HOST,
            'PORT': PORT,
            'USER': USER,
            'PASSWORD': PASSWORD,
            'TEST': {
                'NAME': "test_{}".format(NAME)
            }
        }
    }

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

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
