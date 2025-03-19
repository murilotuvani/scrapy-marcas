import scrapy

class BrandSpider(scrapy.Spider):
    name = 'brandsInfoSpider'
    start_urls = ['https://www.rankingthebrands.com/Brand-detail.aspx?brandID=6572'
                  ,'https://www.rankingthebrands.com/Brand-detail.aspx?brandID=5919']

    def parse(self, response):
        brand_data = {}
        #  ctl00_mainContent_LBBrandIndustry
        for info_row in response.css('.brandInfoRow'):
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

        yield brand_data

