# datasnapper

A simple Python tool to gather and collect text from websites, extracting and storing information from websites in an unstructured text output format.

The objective is to ingest data into a Large Language Model (LLM) vector database, facilitating machine learning tasks within AI applications as LangChain.

NB. Currently testing with a locally running LLM, LangChain and vector database setup.

## Installation

Install via Git clone:

```bash
git clone 

```

## Usage

```bash
python3 datasnapper.py -h
usage: datasnapper.py [-h] [--max_depth MAX_DEPTH] --output_file OUTPUT_FILE url

Web Scraper with Recursive Crawling

positional arguments:
  url                   URL of the website to scrape recursively

optional arguments:
  -h, --help            show this help message and exit
  --max_depth MAX_DEPTH
                        Maximum depth for recursive crawling, default is 2
  --output_file OUTPUT_FILE
                        Output file to save scraped text
````

Example:

```bash
python3 datasnapper.py "https://www.opencve.io/cve?cvss=critical&search=" --output_file cve_scrape_datasnapper.txt --max_depth 2
`````



### Todo

* Implement option to input user supplied HTTP Headers in order to extract data from web apps behind authentication.
* Better error handling
* Implement rate limit of http requests


# Disclaimer

Please be aware of the following points regarding the use of tool:

* Respect Website Policies: 
Ensure that you respect the terms of use, privacy policies, and copyright restrictions of the websites you crawl. Unauthorized crawling of websites may violate legal and ethical guidelines.

* Use at Your Own Risk: 
The tool is provided as-is without any warranties, express or implied. I do not guarantee the availability, performance, or suitability of datasnapper Web Crawler for any specific purpose.

* Liability Limitation: 
We shall not be liable for any damages, losses, or liabilities arising from the use of DataSnapper Web Crawler or the data collected through it.

By using DataSnapper Web Crawler, you agree to abide by this disclaimer and take full responsibility for the consequences of your actions. If you do not agree with this disclaimer, refrain from using this tool.

Please use responsibly and respect the rights and policies of the websites you crawl. 

