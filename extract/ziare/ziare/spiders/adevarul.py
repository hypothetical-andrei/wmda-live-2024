import scrapy


class AdevarulSpider(scrapy.Spider):
    name = "adevarul"
    allowed_domains = ["adevarul.ro"]
    start_urls = ["https://adevarul.ro"]

    def parse(self, response):
        for url in ["https://adevarul.ro"]:
            yield scrapy.Request(url = url, callback = self.parse_page)

    def parse_page(self, response):
        for link in response.css('[data-gtrack]'):
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        article_text = response.css('main')
        raw_text = article_text.get()
        yield {
            'text': raw_text
        }