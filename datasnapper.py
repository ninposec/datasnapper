import argparse
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin

def get_domain(url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"

def clean_text(text):
    # Remove unusual line terminators and replace with newline characters
    cleaned_text = re.sub(r'[\u200b-\u200d\u2028-\u2029\u0085]+', '\n', text)

    # Remove big blank lines
    cleaned_text = re.sub(r'\n\s*\n', '\n\n', cleaned_text)

    return cleaned_text

def crawl_website(url, base_url_path, max_depth=2, visited_urls=None):
    if visited_urls is None:
        visited_urls = set()

    data = []

    def _crawl(url, depth):
        if depth > max_depth or url in visited_urls:
            return

        print(f"Visiting: {url}")
        visited_urls.add(url)

        response = requests.get(url)
        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        all_text = soup.get_text()
        data.append(clean_text(all_text))  # Clean the text before appending

        # Extract text from html tags
        paragraph_tags = soup.find_all(['p', 'h4','td'])  # elements to extract text from
        for tag in paragraph_tags:
            text = clean_text(tag.get_text())  # Clean the text before appending
            print(f"Extracted from {tag.name}: {text}")
            data.append(text)

        links = soup.find_all('a', href=True)
        for link in links:
            next_url = urljoin(url, link['href'])
            parsed_next_url = urlparse(next_url)
            parsed_base_url_path = urlparse(base_url_path)
            if parsed_next_url.path.startswith(parsed_base_url_path.path):
                _crawl(next_url, depth + 1)

    _crawl(url, 0)
    return '\n'.join(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Scraper with Recursive Crawling")
    parser.add_argument("url", help="URL of the website to scrape recursively")
    parser.add_argument("--max_depth", type=int, default=2, help="Maximum depth for recursive crawling, default is 2")
    parser.add_argument("--output_file", required=True, help="Output file to save scraped text")

    args = parser.parse_args()

    website_url = args.url
    max_depth = args.max_depth
    output_file = args.output_file

    parsed_url = urlparse(website_url)
    base_url_path = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"  # Using the URL path as the base URL

    scraped_data = crawl_website(website_url, base_url_path, max_depth)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(scraped_data)

    print(f"Web crawling and saving to {output_file} complete.")
