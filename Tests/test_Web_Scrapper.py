# Python test for LLM file

import sys
import os
import pytest
sys.path.insert(0, '../')
import Web_Scrapper as w

# Test Case: make sure that there is 20 headlines scrapped in data.txt 
with open('../inputs/data.txt', "r") as file:
    line_count = sum(1 for line in file)
    if line_count < 20:
        print("error: line_count smaller than should be in data.txt")


# Test case: make sure there is info in URL.txt
if os.path.getsize('../inputs/URLS.txt') == 0:
    print("error: URLS.txt file is empty")

