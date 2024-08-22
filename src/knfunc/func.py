from mindwm import logging
from mindwm.model.events import IoDocument, Pong
from mindwm.knfunc.decorators import iodoc, app

logger = logging.getLogger(__name__)

@iodoc
async def func(iodocument: IoDocument):
    logger.info(f"ping received")
    res = Pong()
    logger.info(f"reply with: {res}")
    return res
