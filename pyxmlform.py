# PeterSZ, prikaz na skontrolovanie spravnosti zapisu XML suboru

from lxml import etree
import sys
import os

cwd = os.getcwd()

if len(sys.argv) != 2:
    print("\nZadajte len 1 argument: xmlfile.xml")
else:
    filename = cwd + "\\" + sys.argv[1]
    xmlFile = open(filename, "r", encoding = "utf-8")
    xmlText = xmlFile.read().encode()
    xmlFile.close()
    try:
        etree.fromstring(xmlText)
        print("\nXML OK")
        
    except Exception as exception:
        print("\nPROBLEM S FORMATOVANIM XML:" + str(exception))

