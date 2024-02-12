# LinkedIn Jobs Scraper

This project is a web scraper built with Scrapy to extract job listings from LinkedIn.

## Installation

1. **Install Scrapy**: Make sure to install Scrapy. You can install it via pip:

    ```
    pip install scrapy


2. **Install Twisted**: Install a specific version of Twisted (22.10.0) required by Scrapy:

    ```pip install Twisted==22.10.0```


## Usage

To run the LinkedIn Jobs Scraper, follow these steps:

1. **Run the Spider**: Use the following command to start the spider:

    ```scrapy crawl linkedin_jobs```


2. **Customize Search**: You can customize the job title and location in the spider settings.

3. **Data Output**:
- The scraped data is saved in a JSON file.
- Additionally, the data is stored in a PostgreSQL database.

## Methods Used for Bypassing Access Limits

The following methods are used to bypass access limits and ensure successful scraping:
- Fake User Agent: The spider uses a fake user agent to mimic real user behavior.
- Random User Agents List Rotator: Rotates through a list of user agents to avoid detection.
- Random Fake Headers Rotation: Rotates fake headers to make requests appear more natural.
- Proxy Rotation: Utilizes a list of proxies to change IP addresses.
- API Providers of Proxy Endpoints: Accesses proxy endpoints provided by API services.
- ScrapeOps Proxy Rotator: Utilizes the ScrapeOps Proxy Rotator service for rotating proxies.
- ScrapeOps Proxy SDK: Uses the ScrapeOps Proxy SDK for proxy management.

## Additional Notes

- **Automation and Cloud Hosting**: Consider using ScrapyD, ScrapeOps, or ScrapyCloud for automation and cloud hosting. ScrapyD and ScrapeOps are free but require a server, while ScrapyCloud is a paid service that includes server hosting.
