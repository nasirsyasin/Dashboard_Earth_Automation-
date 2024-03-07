import logging


class DBELogUtils:
    logger = logging.getLogger('DBELogger')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[DBE]: %(message)s')

    @staticmethod
    def markError(message):
        DBELogUtils.logger.error(message)

    @staticmethod
    def markErrorAndStop(message):
        DBELogUtils.logger.error(message)
        raise RuntimeError(message)

    @staticmethod
    def markPassed(message):
        DBELogUtils.logger.info(message)

    @staticmethod
    def markFailed(message):
        DBELogUtils.logger.warning(message)

    @staticmethod
    def markFailedAndStop(message):
        DBELogUtils.logger.warning(message)
        raise RuntimeError(message)

    @staticmethod
    def markWarning(message):
        DBELogUtils.logger.warning(message)

    @staticmethod
    def logInfo(message):
        DBELogUtils.logger.info(message)


# Configure logging to write to a file
file_handler = logging.FileHandler('dbe.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(DBELogUtils.formatter)
DBELogUtils.logger.addHandler(file_handler)
