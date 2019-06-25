
import logging

class Annotation(object):
    """
    This class is meant to support Annotation formats in XML only
    New annotation types should inherit this class and implement the data travering of the dictionary
    """
    def __init__(self):
        self.logger = logging.getLogger(self.__name__)



    def isValid(self, xmlPath):
        """
        Check whether a submitted XML is valid against the schema
        :param xmlPath:
        :return:
        """
        self.logger.warning("This method needs to be implemented")
        return False

    def loadXML(self,xmlPath):
        """
        Load the XML into dictionary
        :param xmlPath:
        :return:
        """
        self.logger.warning("This method needs to be implemented")

    def isAnnotationTypeSupported(self,schemaType):
        """
        Check if the annoatation type is supported
        :param schemaType:
        :return:
        """
        self.logger.warning("This method needs to be implemented")
        return False

    def convertToAnnotationType(self, toAnnotationType):
        pass
