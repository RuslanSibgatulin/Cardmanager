from datetime import datetime

from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Card, CardState

logger = get_task_logger(__name__)


@shared_task()
def card_expired():
    count = Card.objects.filter(expiration_at__lte=datetime.now()).update(status=CardState.EXPIRED)
    logger.info("Cards expired %s", count)
