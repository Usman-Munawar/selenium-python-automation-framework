import json

class ConfigReader:
    @staticmethod
    def read_config():
        """
        Reads configuration data from config.json file
        and returns it as a dictionary.
        """
        with open("config/config.json", "r") as file:
            return json.load(file)