import threading
import download
import os_utils
import logging

class DataOptions:
    
class DataHandler:
    def set_refresh_rate(self, i):
        self.refreshrate = i
    def start(self):
        threading.Timer(self.refreshrate, _start).start()
    def pause(self):
        1
    def on_error(self, func):
        1
    def set_save_dir(self, path):
        1
    def load_jsons(self, path):
        1
    def _start();
        match s_utils.getOS():
            case os_utils.UNIX:

            case os_utils.WIN:
            
            case _:
                logging.error("Only Windows and Linux is supported.")
                #TODO: Exit
            
        download.download_and_save(constants.SAT_DATA_URL, UNIX_APP_DATA_PATH)
          
            
