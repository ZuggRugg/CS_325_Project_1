##################################
 # NAME: Shayne Tieman          #
 # EMAIL: shtiema@siue.edu      #
 # SIUE-ID: 422                 #
 # PROJECT-2: Scraping Web Data #
##################################

import requests
from bs4 import BeautifulSoup


## get_Data Class :: Gets the data from input file and reads into list
class get_Data:
    def __init__(self):
        self.urls = []  # Initialize the urls attribute to store URLs

    ## Read file function
    def read_file(self):
        try:
            with open("input.txt", 'r') as f:
                content = f.read()
                self.urls = content.splitlines()  # Assuming each line in input.txt is a URL
                print(self.urls)  # Print the URLs to verify
        except FileNotFoundError:
            print("Error: 'input.txt' not found.")
        return self.urls  # Return the list of URLs

    ## Write file Function, writes to a file
    def write_data(self, outfile, contents):
        try:
            with open(outfile, 'w') as f:
                # Write each result on a new line
                for item in contents:
                    f.write(f"{item}\n")
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
                r = requests.get(url, timeout=10)  # Adding timeout to prevent hanging
                soup = BeautifulSoup(r.content, 'html.parser')

                # Extract all <img> tags and getting the 'alt' attribute
                img_tags = soup.find_all('img')
                alt_texts = [img.get('alt') for img in img_tags if img.get('alt')]  # Only include imgs with alt text

                if not alt_texts:  # If no alt text is found
                    print(f"No alt text found in images on {url}, checking for h2 tags.\n")
                    h3_tags = soup.find_all('h3')  # Find <h3> tags with specific class
                    alt_texts = [h3.get_text(strip=True) for h3 in h3_tags]  # Get the text content of <h3> tags

                    # If no relevant text is found from either, note that no data was retrieved
                    if not alt_texts:
                        alt_texts = [f"No relevant content found on {url}"]

                parsed_results.append(alt_texts)  # Store the results for this URL

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
    data_reader.write_data('output.txt', parsed_data)

    print("Program terminated!")

if __name__ == "__main__":
    main()

