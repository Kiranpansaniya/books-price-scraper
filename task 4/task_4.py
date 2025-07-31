import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'https://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Select all product elements
products = soup.select('article.product_pod')

# Open (or create) a CSV file to store the data
with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price', 'Rating'])  # Write header row

    for product in products:
        name = product.h3.a['title']
        price = product.find('p', class_='price_color').text
        rating_class = product.find('p', class_='star-rating')['class'][1]
        writer.writerow([name, price, rating_class])

print("✅ Product data extracted and saved to products.csv")
