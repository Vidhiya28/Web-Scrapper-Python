# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Importing Scrapy module to define items (objects to be scraped)
import scrapy

# Defining a class to store scraped data for books
class BookscraperItem(scrapy.Item):
    # Placeholder for defining item fields; not used
    name = scrapy.Field()
    pass  # Placeholder that does nothing (can be removed)

# Defining a function to serialize prices (convert to string with currency symbol)
def serialize_price(value):
    return f'£ {str(value)}'

# Defining the actual item class for book data
class BookItem(scrapy.Item):
    # Fields to hold scraped book data
    url = scrapy.Field()  # URL of the book
    title = scrapy.Field()  # Title of the book
    upc = scrapy.Field()  # Universal Product Code
    product_type = scrapy.Field()  # Type of product (e.g., book)
    price_excl_tax = scrapy.Field()  # Price excluding tax
    price_incl_tax = scrapy.Field()  # Price including tax
    tax = scrapy.Field()  # Tax amount
    availability = scrapy.Field()  # Availability status (e.g., In stock)
    num_reviews = scrapy.Field()  # Number of reviews
    stars = scrapy.Field()  # Rating in stars
    category = scrapy.Field()  # Category of the book
    description = scrapy.Field()  # Book description
    price = scrapy.Field()  # Price field (custom serialization could be applied)
