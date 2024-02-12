from urllib.parse import urlencode
import scrapy
from linkedinJobsScraper.items import JobItem
from linkedinJobsScraper.settings import SCRAPEOPS_API_KEY
import random

class LinkedJobsSpider(scrapy.Spider):
    name = "linkedin_jobs"
    allowed_domains = ['linkedin.com', 'https://proxy.scrapeops.io/v1/']
    
    job_title = "Data Engineer"
    location = "worldwide"
    job_title_f = job_title.replace(" ", "%2B")
    location_f = location.replace(" ", "%2B")
    api_url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={job_title_f}&location={location_f}&trk=public_jobs_jobs-search-bar_search-submit&start=0' 
    
    USERAGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]
    
    def start_requests(self):
        job0 = 0
        # first_url = self.api_url + str(job0)
        first_url = self.api_url
        yield scrapy.Request(url=first_url, callback=self.parse_job,
                            headers={"User-Agent": self.USERAGENTS[random.randint(0, len(self.USERAGENTS)-1)]},
                            meta={'first_job_on_page': job0})


    def parse_job(self, response):
        if response.status == 403:
            self.logger.warning("Forbidden response received.")
            return

        job_item = JobItem()
        jobs = response.css("li")
        job_count = 0
        
        
        for job in jobs:
            
            job_item['job_title'] = job.css("h3::text").get(default='not-found').strip()
            job_item['company_name'] = job.css('h4 a::text').get(default='not-found').strip()
            job_item['location'] = job.css('.job-search-card__location::text').get(default='not-found').strip()
            job_item['job_post_url'] = job.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
            job_item['company_link'] = job.css('h4 a::attr(href)').get(default='not-found')
            job_item['date_listed'] = job.css('time::text').get(default='not-found').strip()

        
            self.logger.info(job_item)
            
            yield job_item
            
            job_count += 1
            if job_count >= 20:
                self.logger.info("Maximum limit (20) reached. Stopping further scraping.")
                return
            
            
            

# This can be elimanted when using scrapeops proxy sdk
# replaced the : url=get_proxy_url(first_url)
API_KEY = SCRAPEOPS_API_KEY
def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/' + urlencode(payload)
    return proxy_url