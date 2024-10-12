from pathlib import Path
import pandas as pd
import numpy as np
import json
import scrapy


class CarspiderSpider(scrapy.Spider):
    name = "carspider"

    allowed_domains = ["autotrader.com"]
    #start_urls = ["https://www.autotrader.com"]
    #start_urls = ["https://www.autotrader.com/cars-for-sale/all-cars/cars-between-10000-and-16500/honda/hr-v/austin-tx?newSearch=true&zip=78745"]
    #start_urls = ["https://www.autotrader.com/cars-for-sale/honda/civic/austin-tx?newSearch=false&numRecords=100&zip=78745"]
    #start_urls = ["https://www.autotrader.com/cars-for-sale/honda/civic/austin-tx?newSearch=true&zip=78745"]
    start_urls = ["https://www.autotrader.com/cars-for-sale/cars-between-10000-and-16500/honda/austin-tx?modelCode=CIVIC&modelCode=HONHRV&modelCode=ACCORD&newSearch=true&numRecords=100&zip=78745"]
    def parse(self, response):
        filename = "honda-civics.html"
        #filename = "honda-hrvs.html"
        #filename = "autotrader.html"
        Path(filename).write_bytes(response.body)
        item_dict = json.loads(response.xpath('//script[@data-cmp="listingsCollectionSchema"]//text()').get())
        items = item_dict['about']['offers']['itemOffered']
        print(items[0])
        item_count = len(items)
        vin, year, make, model, price, exterior, interior, miles, url, dealer, phone = [], [], [], [], [], [], [], [], [], [], []
        zipcode, address = [], []
        for i in list(range(item_count)):
            item = items[i]
            vin.append(item['vehicleIdentificationNumber'])
            year.append(item['vehicleModelDate'])
            make.append(item['brand']['name'])
            model.append(item['model'])
            price.append(item['offers']['price'])
            exterior.append(item['color'])
            interior.append(item['vehicleInteriorColor'])
            miles.append(item['mileageFromOdometer']['value'])
            url.append(item['url'])
            dealer.append(item['offers']['seller']['name'])
            phone.append(item['offers']['seller']['telephone'])
            address.append(item['offers']['seller']['address']['streetAddress'])
            zipcode.append(item['offers']['seller']['address']['postalCode'])
            print(items[i]['vehicleIdentificationNumber'])
        data = [vin, year, make, model, price, exterior, interior, miles, url, dealer, phone, address, zipcode]
        #print(np.transpose(data))
        df = pd.DataFrame(np.transpose(data), columns=['vin', 'year', 'make', 'model', 'price', 'exterior', 'interior', 'miles', 'url', 'dealer', 'phone', 'address', 'zipcode'])
        df.to_csv('out.csv', index=False)

#data = json.loads(response.xpath('//script[@data-cmp="listingsCollectionSchema"]//text()').get())
#data['about']['offers']['itemOffered'][0]

#car_data = json.loads(response.xpath('.//*[contains(text(),"vehicleIdentification")]/text()').get())

#In [32]: car_data['about']
#Out[32]: 
#{'@type': 'WebPage',
# 'name': 'Honda HR-V for Sale in Austin, TX',
# 'offers': {'@type': 'Offer',
#  'itemOffered': [{'@type': ['Product', 'Car'],
#    'vehicleIdentificationNumber': '3CZRU5H58GM721063',
#    'name': 'Used 2016 Honda HR-V EX',
#    'mpn': 'Used 2016 Honda HR-V EX',
#    'image': 'https://images.autotrader.com/hn/c/82cfa93d7f594eab950007b2c3a1d1eb.jpg',
#    'itemCondition': 'http://schema.org/UsedCondition',
#    'offers': {'@type': 'Offer',
#     'priceCurrency': 'USD',
#     'price': '15592.00',
#     'availability': 'http://schema.org/InStock',
#     'url': 'https://www.autotrader.com/cars-for-sale/vehicle/725507668',
#     'seller': {'@context': 'http://schema.org/',
#      '@type': 'AutoDealer',
#      'name': 'AutoNation Chevrolet West Austin',
#      'telephone': '18882047605',
#      'address': {'@context': 'http://schema.org/',
#       '@type': 'PostalAddress',
#       'addressLocality': 'Austin',
#       'addressRegion': 'TX',
#       'postalCode': '78759',
#       'streetAddress': '11400 RESEARCH BLVD'}}},
#    'brand': {'@type': 'Brand', 'name': 'Honda'},
#    'model': 'HR-V',
#    'manufacturer': {'@context': 'http://schema.org/',
#     '@type': 'Organization',
#     'name': {'code': 'HONDA', 'name': 'Honda'}},
#    'vehicleModelDate': 2016,
#    'driveWheelConfiguration': '2 Wheel Drive - Front',
#    'vehicleEngine': '4-Cylinder',
#    'vehicleTransmission': 'Continuously Variable Automatic',
#    'color': 'Gray',
#    'mileageFromOdometer': {'@type': 'QuantitativeValue',
#     'value': '87,845',
#     'unitCode': 'SMI'},
#    'url': 'https://www.autotrader.com/cars-for-sale/vehicle/725507668',
#    'vehicleInteriorColor': 'Black',
#    'fuelEfficiency': '28 City / 34 Highway',
#    'fuelType': {'code': 'G', 'group': 'Gas', 'name': 'Gasoline'},
#    'sku': 725507668,
#    'description': 'Location: Austin, TX. This 2016 Honda HR-V is listed for $15592'}]}}
