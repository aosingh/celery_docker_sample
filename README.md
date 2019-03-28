This is a sample project-structure which you can follow if you plan to 
use Celery as an Asynchronous distributed Task Queue. 


## Pre-requisites

Please install the following for project setup

1. docker
2. docker-compose
3. python3
4. virtualenv

## Breakdown of services.

### Task
A celery task is any callable. You can define a celery task using `@task` decorator.
For this sample project, please refer the `tasks/__init__py` file for an example of a task.
Tasks should never be executed in a blocking manner. They are queued and then executed by a celery
worker instance. 

If your task is I/O bound then you can add a timeout period to avoid permanently blocking the worker executing the task. 

If your task is CPU intensive then adding more number of workers will help improve the throughput.
In the `docker-compose.yaml` we schedule a task using the following service.

```
task_scheduler:
    image: celery_poc:test
    command: python scheduler.py
    env_file: env.sh
    depends_on:
      - celery_broker
      - celery_backend
```

### Worker
A worker is an instance of your application which has access to the resources to execute the task.
When you start a celery worker by default the concurrency factor is number of cores on your system.
You can limit the concurrency factor using the `-c` option. 
In the `docker-compose.yaml` we start a worker instance using the following command. 

```
worker:
    image: celery_poc:test
    command: celery worker -A tasks -Q url -l info -Ofair
    env_file: env.sh
    depends_on:
      - celery_backend
      - celery_broker
```


### Message Broker
Tasks are queued and an instance of a celery worker monitors the queue and executes the tasks in that queue. 
This queue is called the Message Broker. We use `redis` as a message queue which will be in-memory. 
However, with docker volumes the broker state will be persisted in between restarts.

```
celery_broker:
    image: redis:3-alpine
    command: redis-server --appendonly yes
    ports:
      - "6379:6379"
    volumes:
      - "celery_broker_data:/data"
```


### Tasks Result Backend
Tasks results, stats and tracebacks are saved in the result backend. Celery gives multiple options. 
We use `postgres`

```
  celery_backend:
    image: postgres:latest
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: docker
      POSTGRES_PASSWORD: docker
    volumes:
      - "celery_backend_data:/var/lib/postgresql/data"
```



