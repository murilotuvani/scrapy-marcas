import scrapy
import string
from pymongo import MongoClient

class BrandSpider(scrapy.Spider):
    name = 'brandsSpider'
    start_urls = []
    alphabet_range = list(string.ascii_uppercase)

    for letter in alphabet_range:
        url = 'https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter=' + letter
        start_urls.append(url)

    def __init__(self, *args, **kwargs):
        super(BrandSpider, self).__init__(*args, **kwargs)
        self.client = MongoClient('localhost', 27017)  # Adjust the connection string as needed
        self.db = self.client['brand_database']
        self.collection = self.db['brands']

    def parse(self, response):
        for brandline in response.css('.brandLine'):
            href = brandline.css('a::attr(href)').get()
            brand_name = brandline.css('a span::text').get()
            brand_data = {'Brand URL': href, 'Brand Name': brand_name}
            href = 'https://www.rankingthebrands.com/'+ href
            yield scrapy.Request(url=href, callback=self.parse_brand_details, meta={'brand_data': brand_data})

    def parse_brand_details(self, response):
        brand_data = response.meta['brand_data']

        info_rows = response.css('.brandInfoRow')
        if info_rows is not None:
            for info_row in info_rows:
                hc = info_row.css('.brandInfoLabel span::text');
                info = None
                if hc is not None:
                    info = hc.get()

                hc = info_row.css('.brandInfoLabel span a::text')
                if info is None and hc is not None:
                    info = hc.get()

                hc = info_row.css('.brandInfoText span::text')
                value = None
                if hc is not None:
                    value = hc.get()

                hc = info_row.css('.brandInfoText span a::text')
                if value is None and hc is not None:
                    value = hc.get()

                print('Info  : ' + info if info is not None else 'None')
                print('Value : ' + value if value is not None else 'None')
                if info is not None and value is not None:
                    brand_data[info] = value

        self.collection.insert_one(brand_data)

        yield brand_data