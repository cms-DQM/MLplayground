from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from ..config import common_indexer_queue, primary_datasets, workspaces
from . import celeryconfig


logger = get_task_logger(__name__)

app = Celery("dials_etl")

app.config_from_object(celeryconfig)

app.conf.beat_schedule = {
    "Dataset indexing pipeline": {
        "task": "dataset_indexer_pipeline",
        "schedule": crontab(minute=0),
        "options": {"queue": common_indexer_queue},
        "kwargs": {"workspaces": workspaces, "primary_datasets": primary_datasets},
    }
}
