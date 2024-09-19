from DataSaver import DataSaver
from Scraper import Scraper


class App:
    def __init__(self, url, pages):
        self.scraper = Scraper(url, pages)

    def run(self):
        print("Starting Scraping...")
        job_list = self.scraper.scrape()
        if job_list:
            job_data = DataSaver(job_list)
            job_data.save()
        else:
            print('No jobs found')
