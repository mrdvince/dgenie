import os
import secrets
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.token_urlsafe(64)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", True)

# https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts
HOSTS = os.getenv("DJANGO_HOSTS")
ALLOWED_HOSTS = [] if not HOSTS else HOSTS


# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
]
LOCAL_APPS = [
    "core",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#migration-modules
MIGRATION_MODULES = {"core": "core.contrib.core.migrations"}

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
# TODO: switch to redis in production
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/4.0/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/4.0/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(BASE_DIR / "static")]
# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# # http://whitenoise.evans.io/en/latest/django.html
# ------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#media-root
MEDIA_ROOT = str(BASE_DIR / "media")
# https://docs.djangoproject.com/en/4.0/ref/settings/#media-url
MEDIA_URL = "/media/"


# Default primary key field type
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-user-model
AUTH_USER_MODEL = "core.User"

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
# TODO: Uncomment the following line to force all requests to use SSL,
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = os.getenv("DJANGO_SECURE_SSL_REDIRECT", default=False)
# https://docs.djangoproject.com/en/4.0/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/4.0/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/4.0/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.getenv(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = os.getenv("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = os.getenv(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)
# https://github.com/adamchainz/django-cors-headers#cors_allowed_origins-sequencestr
CORS_ALLOWED_ORIGINS = ALLOWED_HOSTS
# https://github.com/adamchainz/django-cors-headers#cors_allow_credentials-bool
CORS_ALLOW_CREDENTIALS = True

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#logging
# See https://docs.djangoproject.com/en/4.0/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
