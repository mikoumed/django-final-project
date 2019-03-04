import os
import dj_database_url
from urllib.parse import urlparse
from .base import *

SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    '^8ai-6gb!yyg19uangdahsi8a%c=)mb0xler7%0klh1mz!^snago;91_')
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['*']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# CELERY/REDIS settings
BROKER_URL = os.environ['REDIS_URL']
# BROKER_VHOST = '0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Casablanca'
CELERY_RESULT_BACKEND = os.environ['REDIS_URL']
CELERY_TASK_IGNORE_RESULT= -1

redis_url = urlparse(os.environ.get('REDIS_URL'))

# REDIS CACHE settings
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://localhost:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
            'OPTIONS': {
                'PASSWORD': redis_url.password,
                'DB': 1,
        }
    }
}

# CELERY BEAT SCHEDULER
CELERY_BEAT_SCHEDULE = {
    'request_api_every_15_min': {
        'task': 'tasks.request_api',
        'schedule': 900.0,
    },
}

CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
