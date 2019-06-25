## Usage example
import logging

from config import Config
from annotationloader import AnnotationLoader
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)
logger = logging.getLogger(__name__)
myconfig=Config()
pascalAnnotator = AnnotationLoader().loadAnnotator('pascalvoc',myconfig)
vaticAnnotator = AnnotationLoader().loadAnnotator('vatic',myconfig)
logger.debug(pascalAnnotator)
logger.debug(vaticAnnotator)