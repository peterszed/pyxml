# PeterSZ, prikaz na validaciu XML s DTD

from lxml import etree
import sys
import os

cwd = os.getcwd()

if len(sys.argv) != 3:
    print("\nZadajte argumenty: xmlFile.xml xmlSchema.xsd")
else:
    xmlFilename = cwd + "\\" + sys.argv[1]
    xmlText = etree.parse(xmlFilename)
    schemaFilename = cwd + "\\" + sys.argv[2]
    schemaText = etree.parse(schemaFilename)
    schemaValidator = etree.XMLSchema(schemaText)

    xmlIsValid = schemaValidator.validate(xmlText)
    
    if xmlIsValid:
        print("\nXML je validny podla XML schemy")
    else:
        print("\nChyba: \n" + str(schemaValidator.error_log.filter_from_errors()[0]))
        
