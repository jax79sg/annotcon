from annotationcsv import AnnotationCSV
from annotationxml import AnnotationXML


class AnnotationLoader(object):

    def loadAnnotator(self, annotationtype, _config):
        """
        Loads the correct annotation object based on the annotation type
        :param annotationtype:
        :param _config:
        :return:
        """

        name, format, type =_config.getAnnotationProperties(annotationtype)
        if (format=='xml'):
            return AnnotationXML(name, _config)
        elif(format=='csv'):
            return AnnotationCSV(name, _config)

