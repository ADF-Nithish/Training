"""
File is helpful for logging
"""
import os
import logging

class Logging:
    """
    This class is used to write all the Logs to a file.
    Attributes
        log_dir : str (path for the log directory file).
    Methods
        write_log(contents) : logging (writes the log to the logfile).
    """
    def __init__(self):
        self.__log_dir = os.path.join(os.getcwd(),"fileparser.log")
    def finish(self):
        """
        Logging Finished
        """
        file = self.__log_dir.split('\\')[-1]
        logging.info(" %s %s",'Finished Logging',file)
    def write_log(self,contents):
        """
        This method is used to write the content to a file.
        """
        logging.basicConfig(
            filename=self.__log_dir,
            filemode='a+',
            format='%(asctime)s - %(message)s',
            level=logging.DEBUG
        )
        logging.debug('%s',contents)
        self.finish()
