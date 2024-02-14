import requests
from bs4 import BeautifulSoup
url1 = "http://next.test4.lizardmonitoring.com:3000/app/location/showSensors?netnum=-5002"

url2 = "https://www.amazon.in/iQOO-Fearless-Snapdragon%C2%AE-Independent-Flagship/dp/B07WHSQWLW/ref=sr_1_2?crid=1OJWG2REFV6ZM&keywords=iq%2Bneo%2B7%2Bpro&qid=1704189280&sprefix=iq%2Bneo%2Caps%2C228&sr=8-2&th=1"

def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
        return None

def get_page_content(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

def get_product_title(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title_tag = soup.find('title')
    return title_tag.text.strip() if title_tag else None

def compare_urls(url1, url2):
    content1 = get_page_content(url1)
    print(content1)
    content2 = get_page_content(url2)
    if content1 is None or content2 is None:
        return "Error fetching content from one or both URLs"

    title1 = get_product_title(content1)
    title2 = get_product_title(content2)

    if title1 and title2:
        if title1 == title2:
            return "Both URLs have the same product title"
        else:
            return "The product titles of the URLs are different"
    else:
        return "Error extracting product title from one or both URLs"

# Example usage with another URL
result = compare_urls(url1, url2)
print(result)
