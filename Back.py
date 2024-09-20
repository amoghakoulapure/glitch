# Import the necessary modules
import scrapy

# Define the Spider class
class MySpider(scrapy.Spider):
    # Name of the spider
    name = "my_spider"

    # Start URL
    start_urls = [
        'https://krama.karnataka.gov.in/reports/state.aspx?',
    ]

    # Define the parse function
    def parse(self, response):
        # Extract the title of the webpage
        title = response.xpath('//title/text()').get()

        # Handle errors
        if title is None:
            print('Error: Unable to extract title')
        else:
            # Print the title
            print('Title:', title)

            # Yield the title
            yield {
                'title': title,
            }
