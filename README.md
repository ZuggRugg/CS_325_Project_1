# Introduction
This is the final project for the CS-325 course 'Software Engineering' 
The Project is to create combine the last two projects and make a project that scrapes the web for data
on different business articles and then runs sentiment anaylsis using LLM models on the data. 

### Technology used
- Python 3.12.3 and above
- the Beautiful Soup, Transformers, Torch, and pytest packages.
- Docker Container

# Setup
The first thing you will need to run this project is some form of virtual environment such as venv or miniconda

Miniconda:
``` python3
conda env update -n my_env --file requirements.yaml
```
or you could use this for Venv or Miniconda after going to the virtual environment you want to use
Venv:
``` python3
pip install -r requirements.yaml
```

then to compile go over to the working directory and use the command

```python3
python main_file.py
```

# Misc
This project uses the basic model that Transformers specifies for you, the pytest files are in the Test directory,
The inputs folder contains the plain-text files for the URLs that you can give it, the data.txt stores the article
headlines. Note that the Web-Scraper can only handle xml files, this is because most websites have still working rss feeds
that have a basic structure that they all share, This makes getting headlines for various websites easy.
To use another website just find the rss feed for your preffered website and paste the URL to the URL.txt file.

# Images
![outputs](https://github.com/ZuggRugg/CS_325_Project_1/blob/final/img/Outputs.png)
