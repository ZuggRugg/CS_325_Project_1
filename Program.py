# -----------------------------------------------------------------------
# Shayne Tieman CS325 Project_1                                         |
# Section 1                                                             | 
# Receive list of responses from two LLM's                              |
# -----------------------------------------------------------------------

import transformers as t
# print("\nMy current version of Transformers:", trans.__version__)

# Data Class :: reads the 'input.txt' and appends it to a list 
class data:
    def __init__(self): 
        self.input_list = [] # where the file contents are stored in the list


    def read_data(self, myfile):
        f = open(myfile, "r", encoding="UTF-8")
        data_read = f.read()
        self.input_list = data_read.split("\n\n")
        # print("\n", self.input_list) just a test in case file reading not working
        f.close()
        

# Model Class :: Contains Information about the current two Prompted Models and Tokenizers used
class models:
    def __init__(self):
        self.model1 = t.AutoModelForCausalLM.from_pretrained('distilbert/distilgpt2')
        self.tokenizer1 = t.AutoTokenizer.from_pretrained('distilbert/distilgpt2')
        # model2 = "different model"

    def response(self):
        generator = t.pipeline(task="text-generation", model=self.model1, tokenizer=self.tokenizer1)
        x = generator("Hi how are you? My name is Jack!")
        print(x)


# Read Data from Text file and append to a list :: data.input_list
Data = data()
Data.read_data("input.txt")

print("\n")

model_instance = models() 
model_instance.response() #generate common response using GPT2 and Llama 




