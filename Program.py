# Shayne Tieman CS325 Project_1
# Use the conda env function that is now installed with the conda.el 
# package use pipeline function that is included with transformers library

# https://huggingface.co/docs/transformers/en/autoclass_tutorial

import transformers
# from transformers import pipeline 
# pipeline, AutoTokenizer
print("\nMy current version of Transformers:", transformers.__version__)


# need to run a pretrained model that is loaded from the package otherwise wont work. 
# Tokenizer converts a string to an input you can insert to the model
# It may also be the case that I am wrong on all this as well (RTFM)


# function to read data from text file
# create variable to store the prompts inside of a list. 
class data:
    input_list = []

    def read_data():
        f = open("input.txt", "r")
        data_read = f.read()
        print("\n", data_read)
        f.close()



# model class that would be used to get two textgen models and read input list. 
# class models:
# transcriber = pipeline(task="automatic-speech-recognition")



data.read_data()



    






