from .base import *


# CELERY/REDIS settings
BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Casablanca'
CELERY_RESULT_BACKEND='redis://localhost:6379/1'
CELERY_TASK_IGNORE_RESULT= -1



# REDIS CACHE settings
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
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
