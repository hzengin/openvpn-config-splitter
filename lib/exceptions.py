class InvalidConfigFile(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return repr("Invalid configuration file")
