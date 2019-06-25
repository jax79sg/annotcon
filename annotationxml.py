
import xmlschema
import logging

class AnnotationXML(object):
    """
    This class is meant to support Annotation formats in XML only
    New annotation types should inherit this class and implement the data travering of the dictionary
    """

    def __init__(self, _schemaType, _config):
        """

        :param _schemaType:
        :param _config:
        """
        self.logger = logging.getLogger(__name__)
        self.schematype=_schemaType
        self.config = _config
        if self.isAnnotationTypeSupported(self.schematype)==False:
            raise Exception("Requested type {} is not supported. \nSupported types: {}".format(self.schematype,self.config.getAnnotationTypes()))

        schemaPath = self.config.getSchemaPath()+'/'+self.schematype+'.xsd'
        self.xs = xmlschema.XMLSchema(schemaPath)
        self.logger.info("Schema {} loaded from {}".format(self.schematype, schemaPath))

    def isValid(self, xmlPath):
        """
        Check whether a submitted XML is valid against the schema
        :param xmlPath:
        :return:
        """
        return self.xs.is_valid(xmlPath)

    def loadXML(self,xmlPath):
        """
        Load the XML into dictionary
        :param xmlPath:
        :return:
        """
        if (self.isValid(xmlPath)):
            self.contentdict=self.xs.to_dict(xmlPath)
        else:
            raise Exception('Content of {} is not of schema {}'.format(xmlPath,self.schematype))


    def isAnnotationTypeSupported(self,schemaType):
        """
        Check if the annoatation type is supported
        :param schemaType:
        :return:
        """
        if schemaType in self.config.getAnnotationTypes():
            return True
        else:
            self.logger.error("Requested type {} is not supported. \nSupported types: {}".format(schemaType,self.config.getAnnotationTypes()))
            return False
