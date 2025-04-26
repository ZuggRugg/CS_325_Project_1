##################################################################################
# Shayne Tieman CS325 Project 3                                                  #
# Section 1                                                                      #
# Run sentiment anaylsis on data scrapped from web                               #
##################################################################################

import torch
import transformers as t

# TODO: Figure out why generating extra response at end (from newline character)
# TODO: add pytests

# Data Class :: reads the 'inputs/data.txt' and appends it to a list ----------------
class data:
    def __init__(self):
        self.input_list = [] # where the file contents are stored in the list

    def read_data(self, myfile):
        f = open(myfile, "r", encoding="UTF-8")
        data_read = f.read()
        self.input_list = data_read.split("\n")
        # print("\n", self.input_list) just a test in case file reading not working
        f.close()


    #TODO Modify output to be more legible for viewing
    def write_data(self, outfile, contents):
        with open(outfile, 'w') as outfile:
            outfile.write('\n'.join(str(i) for i in contents))
            outfile.close()
# End of Class ---------------------------------------------------------------

       
# Model Class :: Runs sentiment anaylsis using basic pre-trained model from package
class models:
    def __init__(self):
        self.output_list = []

    def sentiment_anaylsis(self, input_list):
            classifier = t.pipeline("sentiment-analysis")

            for i in input_list:
                result = classifier(i)[0]
                self.output_list.append(result['label'])
                # print(input_list[i], "\n", output_list[i], "\n")

# End of Class ---------------------------------------------------------------


# Read Data from Text file and append to a list :: data.input_list
# then write to the sentiment_anaylsis file all the 'positive' or 'negative' scores
def main():
    Data = data()
    Data.read_data("inputs/data.txt")
    input_list = Data.input_list


    model_instance = models()
    model_instance.sentiment_anaylsis(input_list)
    
    output = model_instance.output_list
    
    Data.write_data('inputs/sentiment_anaylsis.txt', output)

if __name__ == "__main__":
    main()


