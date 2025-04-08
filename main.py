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
            self.urls = content.splitlines()  # Assuming each line in input.txt is a URL or a block of data
            print(self.urls)
            f.close()
            return self.urls
## end of class :: ----------------------------------



## parse_data Class :: parse's the data with the beautiful soup package
class parse_Data:
    def __init__(self):
        pass

    def soup_data(self):
        parsed_results = []
        # Loop through the data (Assuming data is HTML content in this case)
        for html_content in self.data:
            soup = BeautifulSoup(html_content, 'html.parser')
            # Example parsing: Extracting all the links (anchor tags) from the HTML
            links = soup.find_all('h1')
            parsed_results.append([link.get('href') for link in links])  # Storing all links in the result
        return parsed_results


## end of class :: ---------------------------------



# class WebSrapper():
# r = requests.get(URL)
# print(r.content)

# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.)

# print(soup.prettify())


newOne = get_Data()
newOne.read_file()



print("program terminated!")
