###########################
# Name: Shayne Tieman     #
# Email: shtiema@siue.edu #
# ID: 9422                #
###########################
 
import Web_Scrapper as w
import LLM as l

def main():
    # Web-Scraping part of code that gets article headlines ------
    # Read data (URLs) from input.txt
    data_reader = w.get_Data()
    urls = data_reader.read_file()

    # TODO: make this a pytest thing
    if not urls:
        print("No URLs found in input.txt. Exiting program.")
        return


    # Parse the URLs using BeautifulSoup
    parser = w.parse_Website(urls)
    parsed_data = parser.soup_data()  # Get parsed results
    
    
    print('\n\n')

    # Write results to output.txt
    data_reader.write_data('inputs/data.txt', parsed_data)
    # ------------------------------------------------------------


    # LLM part of code that provides sentiment anaylsis ----------
    Data = l.data()
    Data.read_data("inputs/data.txt") 
    input_list = Data.input_list


    model_instance = l.models()
    model_instance.sentiment_anaylsis(input_list)
    
    output = model_instance.output_list
    
    Data.write_data('inputs/sentiment_anaylsis.txt', output)
    # -----------------------------------------------------------

if __name__ == "__main__":
    main()
