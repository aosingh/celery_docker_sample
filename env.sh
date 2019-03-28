CELERY_BROKER_URL=redis://celery_broker:6379
CELERY_BACKEND_URL=db+postgresql+psycopg2://docker:docker@celery_backend:5432
C_FORCE_ROOT=1