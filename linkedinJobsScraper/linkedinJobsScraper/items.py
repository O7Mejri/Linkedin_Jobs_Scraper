# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LinkedinscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(scrapy.Item):
    job_title = scrapy.Field()
    company_name = scrapy.Field()
    location = scrapy.Field()
    job_post_url = scrapy.Field()
    company_link = scrapy.Field()
    date_listed = scrapy.Field()
