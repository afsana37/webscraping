import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('p')[0].get_text())

page1 = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup1 = BeautifulSoup(page1.content, 'html.parser')
print(soup1.find_all(id="first"))



