## to Test
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

# check
# https://stackoverflow.com/questions/18831380/how-can-i-from-bs4-import-beautifulsoup

xml = 'file:///home/ben/Dokumente/enwiki-20220101-pages-articles-multistream/enwiki-20220101-pages-articles-multistream.xml'
url = 'https://en.wikipedia.org/wiki/English_Wikipedia'
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')
#print(isinstance(soup.text, str))


filename = '../../../../Dokumente/enwiki-20220101-pages-articles-multistream/enwiki-20220101-pages-articles-multistream.xml'

#with open(filename, 'r') as f:
    # print(f)
    # _io.TextIOWrapper Attributes




# ElementTree instead of BeautifulShop: 
# https://stackoverflow.com/questions/14924200/loading-huge-xml-files-and-dealing-with-memoryerror
# Example Usage: https://gist.github.com/dsaiztc/6c03f7c30f14d45a6501

parser = ET.iterparse(filename)
print(parser)

for event, element in parser:
    # element is a whole element
#   tag = elem.tag
#   text = elem.text
#   attrs = elem.attrib

   print(element)
#    if element.tag == 'yourelement'
#         # do something with this element
#         # then clean up
# element.clear()