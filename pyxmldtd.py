# PeterSZ, prikaz na validaciu XML s DTD

from lxml import etree
import sys
from io import StringIO
import os

cwd = os.getcwd()

if len(sys.argv) != 3:
    print("\nZadajte argumenty: xmlFile.xml dtdFile.dtd")
else:
    xmlFilename = cwd + "\\" + sys.argv[1]
    xmlText = etree.parse(xmlFilename)
    
    dtdFilename = cwd + "\\" + sys.argv[2]
    dtdFile = open(dtdFilename, "r")
    dtdText = dtdFile.read()
    dtdFile.close()
    dtdText = StringIO(dtdText)

    dtdValidator = etree.DTD(dtdText)

    xmlIsValid = dtdValidator.validate(xmlText)
    if xmlIsValid:
        print("\nXML je validny podla DTD")
    else:
        print("\nChyba: \n" + str(dtdValidator.error_log.filter_from_errors()[0]))
        
