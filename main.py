import requests
from bs4 import BeautifulSoup

# TODO: Get two more local business links and get data from the websites

## get_Data Class :: Gets the data from input file and read into list
class get_Data:
    def __init__(self):
        urls = []

    def read_file(self):
        with open("input.txt", 'r') as f:
            content = f.read()
            print(content)
            f.close()
## end of class :: ----------------------------------



## parse_data Class :: parse's the data with the beautiful soup package
class parse_Data:
    def __init__(self):
        pass

    def soup_data(self):
        print("hello")

## end of class :: ---------------------------------


# URL = ["https://www.bizjournals.com/stlouis/", ""]

# class WebSrapper():

# URL = "http://www.values.com/inspirational-quotes"
# r = requests.get(URL)
# print(r.content)

# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.)

# print(soup.prettify())


newOne = get_Data()
newOne.read_file()


print("program terminated!")
