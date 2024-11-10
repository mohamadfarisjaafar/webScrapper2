import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.qatarairways.com/en-qa/homepage.html'

# Step 1: Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 3: Find the elements you want to scrape
    # For example, find all paragraph tags
    paragraphs = soup.find_all('p')
    
    # Step 4: Extract the desired data
    for paragraph in paragraphs:
        print(paragraph.text)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
