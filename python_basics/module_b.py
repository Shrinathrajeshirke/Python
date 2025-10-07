import logging

def module_b_fn():
    logger = logging.getLogger(__name__)
    logger.info('module B function started')
    logger.debug('this is a debug message from module B')
    logger.info('module B function finished')