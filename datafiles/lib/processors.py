import logging

logger = logging.getLogger(__name__)

def log_enter(section):
	'''processor to print enter section'''

	logger.info('---> %s' % section.uid)

def log_exit(section):
    '''processor to print exit section'''

    logger.info('<--- %s' % section.uid)
    
