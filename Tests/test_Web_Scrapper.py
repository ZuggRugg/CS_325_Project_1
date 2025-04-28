# Python test for LLM file

import sys
import os
import pytest
sys.path.insert(0, '../')
import Web_Scrapper as w

# Test Case: make sure that there is 20 headlines scrapped in data.txt 
def test_line_count():
    with open('../inputs/data.txt', "r") as file:
        line_count = sum(1 for line in file)
        assert line_count == 20, "error: line_count smaller or bigger than should be in data.txt"

# Test case: make sure there is info in URL.txt
def test_URL_exist():
    assert os.path.getsize('../inputs/URLS.txt') > 0, "error: URLS.txt is empty"
