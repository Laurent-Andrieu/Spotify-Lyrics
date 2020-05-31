import requests
from bs4 import BeautifulSoup


class Find:
    def __init__(self, url):
        self.url = url

        # Request the HTML PAGE
        self.page = requests.get(self.url)

        # Create a BeautifulSoup object
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

        # Find the lyrics section
        self.content = self.soup.find(class_='lyrics')

        # Get <br> tag string
        self.lyrics = self.content.getText(separator="\n")

    def print_lyrics(self):
        print(self.lyrics)
