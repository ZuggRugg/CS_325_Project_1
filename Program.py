# -----------------------------------------------------------------------
# Shayne Tieman CS325 Project_1                                         |
# Section 1                                                             |
# Receive list of responses from two LLM's                              |
# -----------------------------------------------------------------------

import torch
import transformers as t

# Data Class :: reads the 'input.txt' and appends it to a list ----------------
class data:
    def __init__(self):
        self.input_list = [] # where the file contents are stored in the list


    def read_data(self, myfile):
        f = open(myfile, "r", encoding="UTF-8")
        data_read = f.read()
        self.input_list = data_read.split("\n\n")
        # print("\n", self.input_list) just a test in case file reading not working
        f.close()


    def write_data(self, outfile, contents):
        with open(outfile, 'w') as outfile:
            outfile.write('\n\n'.join(str(i) for i in contents))
            outfile.close()
# End of Class ---------------------------------------------------------------

       


# Model Class :: Contains Information about the current two Prompted Models and Tokenizers used 
class models:
    def __init__(self):
        self.output_list = []
        self.model1 = t.AutoModelForCausalLM.from_pretrained('distilbert/distilgpt2')
        self.tokenizer1 = t.AutoTokenizer.from_pretrained('distilbert/distilgpt2')

    def gpt2response(self, input_list):
            generator1 = t.pipeline(task="text-generation", model=self.model1, tokenizer=self.tokenizer1)
            for i in range(3):
                x = generator1(input_list[i])
                print('gpt2 output: ', x, '\n')
                self.output_list.append(x)


    def TinyLlama_response(self, input_list):
        self.model2 = t.AutoModelForCausalLM.from_pretrained('TinyLlama/TinyLlama-1.1B-Chat-v1.0')
        generator2 = t.pipeline(task="text-generation", model=self.model1)
        x = generator1(input_list[1])
        print('TinyLlama output: ', x, '\n')
# End of Class ---------------------------------------------------------------


# Read Data from Text file and append to a list :: data.input_list
Data = data()
Data.read_data("input.txt")
input_list = Data.input_list


model_instance = models() 
model_instance.gpt2response(input_list) #generate common response using GPT2 
contents = model_instance.output_list

Data.write_data('output.txt', contents)
