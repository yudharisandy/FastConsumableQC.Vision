import logging
import os

class Logger:
    
    @staticmethod
    def setup_logging():
        logging.basicConfig(
            filename=os.path.join('log', 'log.txt'),
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )