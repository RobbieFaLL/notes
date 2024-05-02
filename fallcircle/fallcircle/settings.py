from pathlib import Path

#base directory for project
BASE_DIR = Path(__file__).resolve().parent.parent
#django uses it for encryption
SECRET_KEY = 'django-insecure-3*sip62c5sw3i1@6)#o&%eosdfky)m66q8@seea4%v+@rr9rsv'
#tells django if you are in development or production mode
DEBUG = True
#who can make requests based in Ip / basic Ip approved list *anyone can view
ALLOWED_HOSTS = []
#modules django comes with
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "pages",
    "blog"
]
#middle applied to all requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#root url config
ROOT_URLCONF = 'fallcircle.urls'
#template engine html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
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
#interface to web server
WSGI_APPLICATION = 'fallcircle.wsgi.application'
#telling django where you database is
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#registration validatiob
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

#internationalisation settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
#static assets - name space
STATIC_URL = 'static/'
#primary key generator
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
