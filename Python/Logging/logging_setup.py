import logging

# used example from https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
logging.basicConfig(datefmt='%F %H:%M:%S', format='%(asctime)s %(levelname)s:%(message)s', encoding='utf-8', level=logging.DEBUG)  # You can also use filename='output.log'

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')