import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        all_quotes = response.css("div.quote")
        
        for quotes in all_quotes:
            content = quotes.css(".text::text").get()
            author = quotes.css(".author::text").get()
            tag = quotes.css(".tag::text").getall()
            
            yield {
                'content':content,
                'author':author,
                'tag':tag
            }
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        else:
            pass  