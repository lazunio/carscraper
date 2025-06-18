# Carscraper
A tool for finding available cars for sale by make/model, zip code, mileage, and price range

It's not intuitive - you have to change the code if you want to change the parameters. And you have
to look on autotrader.com to determine how the makes and models are represented. (see section
"Detailed Instructions" below.)


# Requirements
pip install:
pandas
numpy
scrapy

# Usage
scrapy crawl carspider

This generates a file cars.csv containing the results of the search

# Detailed Instructions
1. Decide what make/model car(s) you want to search for
2. Go to autotrader.com and filter for those makes/models, and inspect the URL for the appropriate strings to use in step 3.
3. Update the make_model values assigned in spiders/carspider.py to the ones you want to search for,
based on what you learned in step 2.
4. Update other configurable variables such as zipcode, max_miles, min_price_dollars, and max_price_dollars
in spiders/carspider.py
5. Run `$scrapy crawl carspider`

