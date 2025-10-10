import logging
import logging.config
from module_a import module_a_fn
from module_b import module_b_fn

def setup_logging():
    log_config = {
        'version':1,
        'formatters':{
            'default':{
                'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        },
        'handlers':{
            'file':{
                'class':'logging.FileHandler',
                'filename':'multi_module.log',
                'formatter':'default',
                'level':'DEBUG'
            },
            'console':{
                'class':'logging.StreamHandler',
                'formatter':'default',
                'level':'DEBUG'
            }
        },
        'root':{
            'handlers':['file', 'console'],
            'level':'DEBUG'
        }
    }
    logging.config.dictConfig(log_config)

if __name__=='__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('main module started')
    module_a_fn()
    module_b_fn()
    logger.info('main module finished')
        