from fastapi.logger import logger


class Logger:
    def error(self, message):
        logger.error(self, message)


    def warning(self, message):
        logger.warning(message)


    def info(self, message):
        logger.info(message)
