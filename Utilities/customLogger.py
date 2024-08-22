import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Log\\"+"automation.log")
        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
        logging.basicConfig(datefmt='%m/%d/%y %I:%M:%S %P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger