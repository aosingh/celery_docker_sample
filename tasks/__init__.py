import celery
import requests

from celery import Celery
from celery.utils.log import get_task_logger

from kombu import Queue

from config import AppConfig

cfg = AppConfig.from_env()

LOG = get_task_logger(__name__)

app = Celery()
app.conf.update(accept_content=['pickle'],
                broker_transport_options={
                    'fanout_prefix': True,
                    'fanout_patterns': True,
                    'visibility_timeout': 3600,
                },
                broker_url=cfg.celery_broker_url,
                result_backend=cfg.celery_backend_url,
                result_persistent=True,
                result_serializer='pickle',
                task_send_event=True,
                task_serializer='pickle',
                task_queues=(Queue('url', routing_key='url'),))


@app.task(bind=True,
          name='tasks.parse_url',
          routing_key='url',
          autoretry_for=(requests.exceptions.HTTPError,),
          retry_backoff=True,
          max_retries=5,
          queue='url',
          acks_late=True)
def parse_url(self, url):
    LOG.info("Received URL %s", url)

    if self.request.retries == self.max_retries:
        LOG.info("Tried maximum of times for URL %s", url)
    else:
        try:
            r = requests.get(url)
            r.raise_for_status()
            LOG.info("Status Code %s", r.status_code)
            LOG.info("Content %s", r.text)
        except requests.exceptions.HTTPError:
            LOG.error("HTTPError while parsing the url %s", url)
            raise
        except Exception:
            LOG.error("Generic Exception while parsing the url %s", url)
            raise
        else:
            LOG.info("Finished Processed %s", url)




