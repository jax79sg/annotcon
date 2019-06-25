import yaml
import logging
class Config(object):
    def __init__(self, configpath='config/config.yaml'):
        """
        Will always load configuration from config/config.yaml
        :param configpath:
        """
        self.logger = logging.getLogger(__name__)
        with open(configpath, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        self.logger.info(self.cfg)


    def getSchemaPath(self):
        """
        Inform config.py where to get the location of XML schemas
        :return:
        """
        return self.cfg['schemas']['location']

    def getAnnotationTypes(self):
        """
        Return all the supported annotation type
        :return:
        """
        annotationTypeList=[]
        for supportedtype in self.cfg['supportedtypes']:
            annotationTypeList.append(supportedtype['name'])
        return annotationTypeList

    def getAnnotationProperties(self, annotationType):
        """
        Get the properties of annotation
        :param annotationType:
        :return: name, format, use type
        """
        for supportedtype in self.cfg['supportedtypes']:
            if (supportedtype['name']==annotationType):
                return supportedtype['name'], supportedtype['format'], supportedtype['use']
        raise Exception("Annotation type {} is not supported\nSupported types: {}".format(annotationType,self.getAnnotationTypes()))