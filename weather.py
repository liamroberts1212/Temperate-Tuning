import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()
#soup = BeautifulSoup(requests.get("https://www.google.com/search?q=weather+london").content)

city = ""
while city != 'q':
    city = input("Enter City: ")
    url = "https://www.google.com/search?q=weather+{}".format(city)
    response = session.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    # store all results on this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get preceipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

    print(result)