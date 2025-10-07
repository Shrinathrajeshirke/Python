import logging.config

def setup_logging_from_file():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    logger.debug('this is a debug message')
    logger.info('this is info message')
    logger.warning('this is warning message')
    logger.error('this is error message')
    logger.critical('this is critical message')

setup_logging_from_file()