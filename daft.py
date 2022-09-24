import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
try:
    # response = requests.get(‘https://www.daft.ie/property-for-sale/blackrock-dublin?terms=&adState=published&numBeds_from=3&numBeds_to=&salePrice_from=&salePrice_to=1500000&showMap=true#3823937’)
    # soup = BeautifulSoup(response.text,‘html.parser’)
    #  # print(soup)
    # # finding parent <ul> tag
    # # parent = soup.find(“body”).find(“ul”,class_=“MapSearchCarousel__CarouselSearchResults-algiji-4”)
    # parent = soup.find((“ul”,class_=“MapSearchCarousel__CarouselSearchResults-algiji-4”)
    # # finding all <li> tags
    # # text = list(parent.descendants)
    # text = list(parent)
    # print(len(text))
    url = 'https://www.daft.ie/property-for-sale/blackrock-dublin?terms=&adState=published&numBeds_from=3&numBeds_to=&salePrice_from=&salePrice_to=1500000&showMap=true#3823937'
    # req = requests.get(url);
    # #<ul data-testid=“mapsearch-carousel” class=“MapSearchCarousel__CarouselSearchResults-algiji-4 fAEcLn”>
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options, executable_path="/Users/user/Desktop/Sundar/chromedriver.exe")
    driver.get(url)
    time.sleep(10)
    page = driver.page_source
    #element = driver.find_element(By.XPATH, "//p[1]")
    element = driver.find_element(By.CLASS_NAME, "TitleBlock__StyledSpan-sc-1avkvav-5")
    print(element.text)
    driver.quit()
except Exception as e:
    print(e)