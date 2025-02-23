# -----------------------------------------------------------------------
# Shayne Tieman CS325 Project_1                                         |
# Section 1                                                             | 
# Receive list of responses from two LLM's                              |
# -----------------------------------------------------------------------

import transformers as trans
# print("\nMy current version of Transformers:", trans.__version__)


# Data Class :: reads the 'input.txt' and appends it to a list 
class data:
    def __init__(self):
        self.input_list = []
        #make append function for list of input data

    def read_data():
        f = open("input.txt", "r", encoding="UTF-8")
        data_read = f.read()
        print("\n", data_read)
        f.close()
        

# Model Class :: Contains Information about the current two Prompted Models and Tokenizers used
class models:
    model1 = "distilgpt2"
    model2 = "different model"

    def response(self):
        generator = trans.pipeline(task="text-generation", model="distilgpt2", tokenizer="distilgpt2")
        x = generator("Hi how are you?")
        print(x)


data.read_data() #Read out the current Input file
new = models() 
new.response() #generate common response using GPT2
