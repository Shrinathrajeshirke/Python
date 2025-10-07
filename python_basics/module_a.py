import logging

def module_a_fn():
    logger = logging.getLogger(__name__)
    logger.info('module A function started')
    logger.debug('this is a debug message from module A')
    logger.info('module A function finished')