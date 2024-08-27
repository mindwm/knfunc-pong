from mindwm import logging
from mindwm.model.events import MindwmEvent
from mindwm.model.objects import Ping, Pong, IoDocument
from mindwm.knfunc.decorators import event, app, Request
from uuid import uuid4

logger = logging.getLogger(__name__)

@event
async def pong(ev: IoDocument):
    logger.info(f"req: {ev}")
    reply = Pong(uuid=ev.uuid)
    logger.info(f"reply with: {reply}")
    return reply
