import json
import logging

class JsonLoader:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {JsonLoader.__name__} was created")


    def LoadConfig(self, config_file):
        self.logger.debug(f"Object: {JsonLoader.__name__}, method: {JsonLoader.LoadConfig.__name__}, start")

        with open(config_file, 'r') as file:
            config = json.load(file)
        
        self.logger.debug(f"Object: {JsonLoader.__name__}, method: {JsonLoader.LoadConfig.__name__}, end")
        return config