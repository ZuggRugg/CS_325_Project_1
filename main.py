import requests
from bs4 import BeautifulSoup

# TODO: get beautful soup package for Python in webScrapping env
# TODO: pip install bs4, then put that into a requirements.yaml


# class get_Data():
    

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.)


# print(soup.prettify())


print("program terminated!")
