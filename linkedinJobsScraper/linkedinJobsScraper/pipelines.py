# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LinkedinjobsscraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        
        # Remove commas from job titles
        if 'job_title' in adapter:
            adapter['job_title'] = adapter['job_title'].replace(',', '')
        
        # Remove duplicates for job_post_url
        processed_urls = set()
        if 'job_post_url' in adapter:
            url = adapter['job_post_url']
            if url in processed_urls:
                self.logger.info(f"Duplicate job post URL found and removed: {url}")
                return None
            processed_urls.add(url)

        return item


import psycopg2
from scrapy.exceptions import NotConfigured

class SaveDataPipeline:
    def __init__(self, database_settings):
        self.database_settings = database_settings
        self.conn = None
        self.cur = None

    @classmethod
    def from_crawler(cls, crawler):
        database_settings = crawler.settings.getdict('DATABASE')
        if not database_settings:
            raise NotConfigured("DATABASE settings is not configured")
        return cls(database_settings)

    def open_spider(self, spider):
        self.conn = psycopg2.connect(**self.database_settings)
        self.cur = self.conn.cursor()
        self.create_table()

    def close_spider(self, spider):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS jobs (
                id SERIAL PRIMARY KEY,
                job_title TEXT,
                company_name TEXT,
                location TEXT,
                job_post_url TEXT,
                company_link TEXT,
                date_listed TEXT
            )
        """
        self.cur.execute(sql)
        self.conn.commit()

    def process_item(self, item, spider):
        sql = """
            INSERT INTO jobs (job_title, company_name, location, job_post_url, company_link, date_listed)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cur.execute(sql, (
            item['job_title'],
            item['company_name'],
            item['location'],
            item['job_post_url'],
            item['company_link'],
            item['date_listed']
        ))
        self.conn.commit()
        return item
