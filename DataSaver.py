import pandas as pd

class DataSaver:
    def __init__(self, job_list):
        self.job_list = job_list

    def save(self, filename="job_listing.csv"):
        file = pd.DataFrame(self.job_list, columns=['Title', 'Company', 'Location', 'Description'])
        file.to_csv(file, index=False)
        print(f"Saved f{file} to f{filename}")


