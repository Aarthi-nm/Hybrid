# import logging
# import os
#
# class LogGen():
#     @staticmethod
#     def loggen():
#         path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
#         logging.basicConfig(filename=path, filemode='a',
#                     format = '%(asctime)s: %(levelname)s:%(message)s', datefmt= '%m%d%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.info("This is a test log entry.")
#         logger.setLevel(logging.DEBUG)
#         return logger

import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        os.makedirs(os.path.dirname(path), exist_ok=True)

        logger = logging.getLogger('customLogger')
        if not logger.handlers:  # Prevent adding multiple handlers
            file_handler = logging.FileHandler(path, mode='a')
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)

        return logger