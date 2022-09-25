import requests
from bs4 import BeautifulSoup
from lxml  import etree
try:
    response = requests.get("https://www.daft.ie/property-for-sale/ireland")
    soup = BeautifulSoup(response.text,'html.parser')
    dom = etree.HTML(str(soup))
    print(dom.xpath([@class,"TitleBlock__Price-sc-1avkvav-4"])'/span.text))

except Exception as e:
    print(e)