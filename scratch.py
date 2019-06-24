from config import Config
from annotationobject import Validator

pascalvocvalidator=  Validator('schemas/pascalvoc.xsd')
vaticvalidator= Validator('schemas/vatic.xsd')

print(pascalvocvalidator.isValid('samples/pascalvoc.xml'))
print(pascalvocvalidator.isValid('samples/vatic.xml'))

myconfig=Config()
