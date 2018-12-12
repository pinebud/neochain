import configparser


class Config(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config/test.ini')

    def get(self, section_name, key):
        return self.config[section_name][key]

