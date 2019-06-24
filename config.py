import yaml
class Config(object):
    def __init__(self, configpath='config/config.yaml'):


        with open(configpath, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        for section in self.cfg:
            print(section)


    def getPathForSchema(self, schemaType):
        return self.cfg[s]