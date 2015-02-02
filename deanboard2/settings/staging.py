from base import *
import dj_database_url

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

DATABASES = {
	'default':dj_database_url.config()
}

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'