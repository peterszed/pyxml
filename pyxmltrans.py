# PeterSZ, prikaz na validaciu XML s DTD

from lxml import etree
import sys
import os

cwd = os.getcwd()

if len(sys.argv) != 4:
    print("\nZadajte argumenty: xmlFile.xml xslFile.xsl outputFormat")
else:
    xmlFilename = cwd + "\\" + sys.argv[1]
    xmlText = etree.parse(xmlFilename)
    transFilename = cwd + "\\" + sys.argv[2]
    transText = etree.parse(transFilename)
    transformXMLWithXSLT = etree.XSLT(transText)
    transformationResult = transformXMLWithXSLT(xmlText)
    outputFilename = cwd + "\\" + sys.argv[2][0 : len(sys.argv[2]) - 4] + "_output." + str(sys.argv[3])
    outputFile = open(outputFilename, "w")
    outputFile.write(str(transformationResult))
    
 
    outputFile.close()
  #  print(transformationResult)

