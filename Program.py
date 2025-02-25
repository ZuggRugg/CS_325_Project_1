# -----------------------------------------------------------------------
# Shayne Tieman CS325 Project_1                                         |
# Section 1                                                             | 
# Receive list of responses from two LLM's                              |
# -----------------------------------------------------------------------

import transformers as trans
# from transformers import pipelin 
# from transformers import pipeline
# print("\nMy current version of Transformers:", trans.__version__)



# Data Class :: reads the 'input.txt' and appends it to a list 
class data:
    def __init__(self):
        self.input_list = []
        #make append function for list of input data

    def read_data(self):
        f = open("input.txt", "r", encoding="UTF-8")
        data_read = f.read()
        print("\n", data_read)
        f.close()
        


# Model Class :: Contains Information about the current two Prompted Models and Tokenizers used
class models:
    def __init__(self):
        self.model1 = trans.AutoModelForCausalLM.from_pretrained('distilbert/distilgpt2')
        self.tokenizer1 = trans.AutoTokenizer.from_pretrained('distilbert/distilgpt2')
        # model2 = "different model"

    def response(self):
        generator = trans.pipeline(task="text-generation", model=self.model1, tokenizer=self.tokenizer1)
        x = generator("Hi how are you? My name is Jack!")
        print(x)


# Data = data()
# Data.read_data()

model_instance = models() 
model_instance.response() #generate common response using GPT2

