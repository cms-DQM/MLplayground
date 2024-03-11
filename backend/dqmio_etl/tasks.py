import logging

from dials import celery_app
from dqmio_file_indexer.models import FileIndex

from .methods import HistIngestion


logger = logging.getLogger(__name__)


@celery_app.task(queue="dqmio_etl_queue")
def ingest_function(file_index: FileIndex):
    ing = HistIngestion(file_index)
    result = ing.run()
    return result
