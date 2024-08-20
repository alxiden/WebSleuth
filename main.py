import requests
from bs4 import BeautifulSoup
import openpyxl

class WebSleuth:
    def __init__(self):
        self.url = None
        self.emails = []
        self.urls = []
        self.phone_numbers = []
        self.names = []
        self.urls = []
        self.documents = []
        self.other = []
        self.harvested = []

    def get_url(self):
        self.url = input("Enter a URL: ")

    def retrieve_website(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            nohtml = soup.get_text()
            urls = soup.find_all('a')
            print("URLs found in the page:")
            for u in urls:
                # Sorting out the URLs
                if u.get('href') == None or u.get('href' in self.harvested):  # If the URL is empty
                    pass
                elif 'https://www.' in u.get('href'):  # If the URL is a full URL
                    self.urls.append(u.get('href'))
                elif '@' in u.get('href'):  # If the URL is an email
                    self.emails.append(u.get('href'))
                elif 'tel:' in u.get('href'):  # If the URL is a phone number
                    self.phone_numbers.append(u.get('href'))
                elif '.pdf' in u.get('href'):
                    self.documents.append(u.get('href'))
                else:  # If the URL is a partial URL
                    self.other.append(u.get('href')) 
                self.harvested.append(u.get('href'))
        else:
            print("Failed to retrieve the website")


    def SecondScan(self):
        for u in self.urls:
            response = requests.get(u)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                nohtml = soup.get_text()
                urls = soup.find_all('a')
                print("URLs found in the page:")
                for u in urls:
                    # Sorting out the URLs
                    if u.get('href') == None or u.get('href') in self.harvested: # If the URL is empty
                        pass
                    elif 'https://www.' in u.get('href'): # If the URL is a full URL
                        self.urls.append(u.get('href'))
                    elif '@' in u.get('href'): # If the URL is an email
                        self.emails.append(u.get('href'))
                    elif 'tel:' in u.get('href'): # If the URL is a phone number
                        self.phone_numbers.append(u.get('href'))
                    elif '.pdf' in u.get('href'):
                        self.documents.append(u.get('href'))
                    else: # If the URL is a partial URL
                        self.other.append(u.get('href'))
                    self.harvested.append(u.get('href'))
    
    def file_writer(self):
        # Create a new workbook
        workbook = openpyxl.Workbook()

        # Create worksheets for URLs, phone numbers, emails, and files
        url_sheet = workbook.create_sheet(title="URLs")
        phone_sheet = workbook.create_sheet(title="Phone Numbers")
        email_sheet = workbook.create_sheet(title="Emails")
        file_sheet = workbook.create_sheet(title="Files")

        # Write data to the worksheets
        for url in self.urls:
            url_sheet.append([url])

        for phone_number in self.phone_numbers:
            phone_sheet.append([phone_number])

        for email in self.emails:
            email_sheet.append([email])

        for file in self.documents:
            file_sheet.append([file])

        # Save the workbook
        workbook.save("/home/user/Documents/WebSleuth/WebSleuth/output.xlsx")
    def main(self):
        self.get_url()
        self.retrieve_website()
        self.SecondScan()
        self.file_writer()


if __name__ == "__main__":
    sleuth = WebSleuth()
    sleuth.main()