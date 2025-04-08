import requests
from bs4 import BeautifulSoup

# TODO: get beautful soup package for Python in webScrapping env
# TODO: pip install bs4, then put that into a requirements.yaml
# TODO: Get two more local business links and get data from the websites



# class get_Data():
# URL = ["https://www.bizjournals.com/stlouis/"]

# class WebSrapper():

    


URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.)


# print(soup.prettify())


print("program terminated!")




