import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url, pages=1):
        self.url = url
        self.pages = pages

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to retrieve {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error while making requests to {url}, {str(e)}")
        return None

    def parse_jobs(self, content):
        webScraper = BeautifulSoup(content, 'html.parser')
        jobs = webScraper.findAll('div', 'job-listing')
        job_list = []
        for job in jobs:
            title = job.find('h2').text.strip()
            company = job.find('div', className="company-name").text.strip()
            location = job.find('div', className="location").text.strip()
            description = job.find('div', className="description").text.strip()
            job_list.append([title, company, location, description])
        return job_list
