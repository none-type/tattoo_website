"""
Django settings for tatweb project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# ////////////////////////SECURITY////////////////////////////
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mLfzamO0kRaesa82zc-1t7nkipdQA5r5HRkFC5Ntd3Qy-nHRENAAv9ea4OJ47QMq_tY'

#SECURE_HSTS_SECONDS = 31536000  # 1 year.  Tells browsers to only interact with your site over HTTPS.
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Also apply to subdomains
#SECURE_HSTS_PRELOAD = True  # Preload HSTS in browsers

#SECURE_SSL_REDIRECT = True # if not set to True, which means your site will allow HTTP traffic instead of redirecting it to HTTPS.

#SESSION_COOKIE_SECURE = True # If session cookies are sent over HTTP, they can be intercepted by attackers, allowing them to hijack user sessions.

#CSRF_COOKIE_SECURE = True #  If the CSRF token is sent over HTTP, it can be intercepted by attackers. This makes it easier for them to carry out CSRF attacks.

#SECURE_BROWSER_XSS_FILTER = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
#X_FRAME_OPTIONS = 'DENY'

#  //////////////////////////CSP///////////////////////////////

CSP_DEFAULT_SRC = ("'self'",)  # Allow resources from the same origin
CSP_SCRIPT_SRC = (
    "'self'", 
    "'unsafe-inline'",  # Allow inline scripts (consider avoiding if possible)
    "https://cdnjs.cloudflare.com"  # For Font Awesome
)
CSP_STYLE_SRC = (
    "'self'", 
    "'unsafe-inline'",  # Allow inline styles (consider avoiding if possible)
    "https://fonts.googleapis.com",  # For Google Fonts
    "https://cdnjs.cloudflare.com"  # For external styles
)
CSP_IMG_SRC = (
    "'self'", 
    "data:",  # Allow data URIs for images if you use them
)
CSP_FONT_SRC = (
    "'self'", 
    "https://fonts.gstatic.com",  # For Google Fonts
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/webfonts/",
)
CSP_CONNECT_SRC = ("'self'",)  # Allow connections to the same origin (for APIs)
CSP_FRAME_SRC = ("'none'",)  # Disallow frames

#CSP_REPORT_URI = '/csp-report/'  # Define an endpoint to handle CSP reports

# ////////////////////////////////////////////////////////////


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # can expose sensitive data in a production environment.

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
    'csp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'tatweb.urls'

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

WSGI_APPLICATION = 'tatweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
