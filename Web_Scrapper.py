##################################
 # NAME: Shayne Tieman          #
 # EMAIL: shtiema@siue.edu      #
 # SIUE-ID: 422                 #
 # PROJECT-2: Scraping Web Data #
##################################

import requests
from bs4 import BeautifulSoup

#TODO: Email Manas about maybe scraping RSS instead becuase its way easier
#TODO: get another RSS feed and rewrite function to accept only 10 feeds per link

## get_Data Class :: Gets the data from input file and reads into list
class get_Data:
    def __init__(self):
        self.urls = []  # Initialize the urls attribute to store URLs

    ## Read file function
    def read_file(self):
        try:
            with open("inputs/URLS.txt", 'r', encoding='utf-8') as f:
                content = f.read()
                self.urls = content.splitlines()  # Assuming each line in input.txt is a URL
                print(self.urls)  # Print the URLs to verify
        except FileNotFoundError:
            print("Error: 'inputs/URLS.txt' not found.")
        return self.urls  # Return the list of URLs

    ## Write file Function, writes to a file
    def write_data(self, outfile, contents):
       try:
        with open(outfile, 'w+', encoding='utf-8') as f:
            for item in contents:
                if isinstance(item, list):
                    for subitem in item:
                        f.write(str(subitem) + '\n')
                else:
                    f.write(str(item) + '\n')
       except IOError as e:
           print(f"Error writing to {outfile}: {e}")



## parse_data Class :: Parse's the data with the BeautifulSoup package
class parse_Website:
    def __init__(self, data):
        self.data = data  # Initialize with the data (the list of URLs)

    def soup_data(self):
        parsed_results = []
        
        # Loop through the URLs (not HTML content)
        for url in self.data:
            print(f"Fetching content from: {url}")
            try:
                # Fetch the HTML content of the URL
                r = requests.get(url, timeout=10)  
                soup = BeautifulSoup(r.content, 'xml')

                # Extract all <img> tags and getting the 'alt' attribute
                items = soup.find_all('item') 
                for item in items:
                    title = item.find('title').text
                    parsed_results.append(title)  # Store the results for this URL

                # If no relevant text is found in RSS, note that no data was retrieved
                if not items:
                    xml_title = [f"No relevant content found on {url}"]
                    parsed_results.append(xml_title)

            except requests.exceptions.RequestException as e:
                print(f"Failed to retrieve {url}: {e}")
                parsed_results.append(f"Failed to fetch {url}")
        
        return parsed_results



## Main function ----------------------------------------------
def main():
    # Read data (URLs) from input.txt
    data_reader = get_Data()
    urls = data_reader.read_file()

    if not urls:
        print("No URLs found in input.txt. Exiting program.")
        return

    # Parse the URLs using BeautifulSoup
    parser = parse_Website(urls)
    parsed_data = parser.soup_data()  # Get parsed results

    # Print parsed results
    print("Parsed Data:")
    for result in parsed_data:
        print(result)

    print('\n')

    # Write results to output.txt
    data_reader.write_data('inputs/data.txt', parsed_data)

    print("Program terminated!")

if __name__ == "__main__":
    main()

