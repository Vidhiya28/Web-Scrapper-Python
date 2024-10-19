import scrapy
from bookscraper.items import BookItem  # Import the BookItem class from the items.py file in the bookscraper project

# Define a new spider class that inherits from scrapy.Spider
class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'  # Name of the spider (used to run it)
    allowed_domains = ['books.toscrape.com']  # Domain restrictions, spider will only scrape this website
    start_urls = ['https://books.toscrape.com/']  # The URL to start scraping from (homepage of the site)

    # Primary parsing method that will be called to process the response
    def parse(self, response):
        # Extract all the book items (each book is contained in an <article> element with the class 'product_pod')
        books = response.css('article.product_pod')

        # Loop through all the books found on the current page
        for book in books:
            # Get the relative URL for each book's detail page (from the <a> tag inside <h3>)
            relative_url = book.css('h3 a ::attr(href)').get()

            # Check if the relative URL already contains 'catalogue/' (the structure changes based on the page)
            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url  # Build the full URL for the book
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url  # Adjust URL if 'catalogue/' is missing

            # Follow the book's detail page and use the parse_book_page method to extract details
            yield response.follow(book_url, callback=self.parse_book_page)

        # Extract the URL of the next page (if available) using the 'next' button at the bottom
        next_page = response.css('li.next a ::attr(href)').get()
        
        if next_page is not None:  # If a next page exists
            # Check if 'catalogue/' is already present in the URL or needs to be added
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page

            # Follow the next page and continue scraping
            yield response.follow(next_page_url, callback=self.parse)

    # Method to parse the individual book detail page
    def parse_book_page(self, response):
        # Extract rows from the table containing book details
        table_rows = response.css("table tr")
        book_item = BookItem()  # Create a new instance of BookItem to store scraped data

        # Assign scraped data to the respective fields in BookItem

        # URL of the book page
        book_item['url'] = response.url,
        
        # Title of the book, extracted from the <h1> tag
        book_item['title'] = response.css('.product_main h1::text').get(),
        
        # UPC (Universal Product Code) of the book, located in the first table row
        book_item['upc'] = table_rows[0].css("td ::text").get()

        # Product type, found in the second table row
        book_item['product_type'] = table_rows[1].css("td ::text").get(),

        # Price excluding tax, found in the third table row
        book_item['price_excl_tax'] = table_rows[2].css("td ::text").get(),

        # Price including tax, found in the fourth table row
        book_item['price_incl_tax'] = table_rows[3].css("td ::text").get(),

        # Tax amount, found in the fifth table row
        book_item['tax'] = table_rows[4].css("td ::text").get(),

        # Availability (stock), found in the sixth table row
        book_item['availability'] = table_rows[5].css("td ::text").get(),

        # Number of reviews, found in the seventh table row
        book_item['num_reviews'] = table_rows[6].css("td ::text").get(),

        # Star rating of the book, extracted from the class attribute of <p> with class 'star-rating'
        book_item['stars'] = response.css("p.star-rating").attrib['class'],

        # Category of the book, extracted from the breadcrumb navigation bar
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),

        # Description of the book, found just after the 'product_description' div
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),

        # Final displayed price, extracted from the price color class
        book_item['price'] = response.css('p.price_color ::text').get(),

        # Return the populated BookItem with all the scraped data
        yield book_item