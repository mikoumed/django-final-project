web: gunicorn headlines.wsgi
worker: celery -A headlines worker -events -loglevel info
beat: celery -A headlines beat 
