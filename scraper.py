import requests
from requests import get
from bs4 import BeautifulSoup  as soup
import pandas 
import numpy
import re
import json


def scrape(url):
        headers = {"Accept-Language":"en-US, en;q=0.5"}
        results = requests.get(url,headers=headers)
        results_soup = soup(results.text, 'lxml')
        priceinfo = results_soup.select("[type='application/ld+json']")[1]
        propinfo = results_soup.select("[type='application/ld+json']")[2]
        priceJson = json.loads(priceinfo.text)['mainEntity']
        price = priceJson['offers'][0]['priceSpecification']['price']
        sqft = int(json.loads(propinfo.text)["floorSize"]['value'].replace(",", ""))
        rooms = int(json.loads(propinfo.text)["numberOfRooms"]['value'])
        bathrooms = json.loads(propinfo.text)['numberOfBathroomsTotal']
        location = json.loads(propinfo.text)['address']['addressLocality']
        pricePerSqft = int(price)/int(sqft)
        lat = json.loads(propinfo.text)['geo']['latitude']
        lon = json.loads(propinfo.text)['geo']['longitude']
        end = []
        end.append([price,sqft,rooms,bathrooms,location,pricePerSqft])
        # df = pandas.DataFrame(end)
        return end


if __name__ == "__main__":
        frame = scrape("https://www.bayut.com/property/details-7557674.html")
        print(frame)
