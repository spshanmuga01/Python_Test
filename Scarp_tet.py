import requests
from bs4 import BeautifulSoup

try:
    response = requests.get('https://www.daft.ie/property-for-sale/blackrock-dublin?terms=&adState=published&numBeds_from=3&numBeds_to=&salePrice_from=&salePrice_to=1500000&showMap=true#3823937')
    soup = BeautifulSoup(response.text,"html.parser")
    print(soup)
    apartments = soup.find('div',class_="MapSearchCarousel__MapCarouselContainer-algiji-3 cVQyWr")
    print(apartments)
except Exception as e:
    print(e)