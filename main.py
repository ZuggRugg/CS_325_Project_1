##############################
# NAME: Shayne Tieman        #
# EMAIL: shtiema@siue.edu    #
# SIU-ID: 422                #
# PROJECT: Scraping Web Data #
##############################

import requests
from bs4 import BeautifulSoup


## get_Data Class :: Gets the data from input file and reads into list
class get_Data:
    def __init__(self):
        self.urls = []  # Initialize the urls attribute to store URLs

    def read_file(self):
        with open("input.txt", 'r') as f:
            content = f.read()
            self.urls = content.splitlines()  # Assuming each line in input.txt is a URL
            print(self.urls)  # Print the URLs to verify
            f.close()
        return self.urls  # Return the list of URLs

    def write_data(self, outfile, contents):
        with open(outfile, 'w') as outfile:
            outfile.write('\n'.join(str(i) for i in contents))
            outfile.close()



## parse_data Class :: Parse's the data with the BeautifulSoup package
class parse_Southern:
    def __init__(self, data):
        self.data = data  # Initialize with the data (the list of URLs)

    def soup_data(self):
        parsed_results = []
        
        # Loop through the URLs (not HTML content)
        for url in self.data:
            print(f"Fetching content from: {url}")
            try:
                # Fetch the HTML content of the URL
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'html.parser')

                # Example parsing: Extracting all <img> tags and getting the 'alt' attribute
                img_tags = soup.find_all('img')
                alt_texts = [img.get('alt') for img in img_tags if img.get('alt')]  # Only include imgs with alt text

                if not alt_texts:  # If no alt text found, add a note
                    alt_texts.append("No alt text available")

                parsed_results.append(alt_texts)  # Store the alt text list for each URL

            except requests.exceptions.RequestException as e:
                print(f"Failed to retrieve {url}: {e}")
                parsed_results.append(f"Failed to fetch {url}")
        
        return parsed_results  # Return the parsed results







## Main function ----------------------------------------------
def main():

    # Read data (URLs) from input.txt
    data_reader = get_Data()
    urls = data_reader.read_file()

    # Parse the URLs using BeautifulSoup
    parser = parse_Southern(urls)
    parsed_data = parser.soup_data()  # Get parsed results


    # Print parsed results
    print("Parsed Data:")
    for result in parsed_data:
        print(result)
        
    
    data_reader.write_data('output.txt', parsed_data) ## write to output file

    print("Program terminated!")

if __name__ == "__main__":
    main()

