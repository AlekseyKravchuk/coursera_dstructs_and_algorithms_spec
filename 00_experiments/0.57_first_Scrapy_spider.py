import scrapy
from scrapy.crawler import CrawlerProcess


class DCspider(scrapy.Spider):
    name = "dc_cpider"

    def start_requests(self):
        urls = 'https://www.datacamp.com/courses/all'
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse())

    def parse(self, response):
        html_file = 'DC_courses.html'
        with open(html_file, 'wb') as fout:
            fout.write(response.body)


if __name__ == '__main__':
    # initiate a CrawlerProcess
    process = CrawlerProcess()

    # tell the process which spider to use
    process.crawl(DCspider)

    # start the crawling process
    process.start()


