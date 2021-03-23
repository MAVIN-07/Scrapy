# Created by Sambit Kumar Mishra 24 March 2021

# Import the required modules
import scrapy
from ..items import HouseOfIndyaItem


# Create a class for the scrapy spider application
class jewellerySpider(scrapy.Spider):
    name = 'jewellery'
    # URL of the site which has to be scraped
    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat'
    ]

    def parse(self, response):
        """Parsing the response from the website

        Args:
            response : Response from the website

        Yields:
            dictionary : key-value pairs
        """

        # Create an instance of class 'HouseOfIndyaItem' (located in items.py)
        items = HouseOfIndyaItem()

        # The collection of necklace_set available
        necklace_set = response.css('#JsonProductList')

        # The total number of necklace_set available in the store
        total_items = int(response.css('.totalRecords::text').extract()[0])

        for i in range(total_items):
            # Description of the necklace set
            description = necklace_set.css('p::text')[i].extract()

            # Price of the necklace set
            price = necklace_set.css('span:nth-child(1)::text')[i].extract()

            # URL of the image of necklace set
            image_url = necklace_set.css(
                '.lazy::attr(data-original)')[i].extract()

            # Store in 'items' instance
            items['description'] = description
            items['price'] = price
            items['image_url'] = image_url

            yield items
