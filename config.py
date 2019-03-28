import os


class AppConfig(object):

    """
    Access environment variables here.

    """

    @classmethod
    def from_env(cls):

        keys = ('celery_broker_url',
                'celery_backend_url')

        kwargs = {k: os.environ.get(k.upper()) for k in keys}
        return cls(**kwargs)

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

