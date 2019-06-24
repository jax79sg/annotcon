
import xmlschema

class AnnotationObject(object):
    schemaPath=None

    def __init__(self, schemaType, config):

        self.xs = xmlschema.XMLSchema(schemaPath)

    def isValid(self, xmlPath):
        return self.xs.is_valid(xmlPath)

    def loadXML(self,xmlPath):
        if (self.isValid(xmlPath)):
            pass
        else:
            raise Exception('Content of {} is not of schema {}'.format(xmlPath,))




