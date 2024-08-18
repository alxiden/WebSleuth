import requests
from bs4 import BeautifulSoup



def main():
    url = input("Enter a URL: ")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        nohtml = soup.get_text()
        urls = soup.find_all('a')
        print("URLs found in the page:")
        for u in urls:
            print(u.get('href'))
        print(nohtml)
    else:
        print("Failed to retrieve the website")

if __name__ == "__main__":
    main()