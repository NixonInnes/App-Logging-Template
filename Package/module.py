from . import get_logger

logger = get_logger(__name__)


def do_something():
    logger.debug('debug log')
    logger.info('info log')
    logger.warning('warning log')
    logger.error('error log')
