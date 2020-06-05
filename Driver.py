import time
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Link:
    def __init__(self, path):
        """

        :type path: raw str
        """
        self.url = 'https://genius.com/'
        self.gecko_path = path
        self.state = dict(running=False, error=None)
        self.wh = None
        self.driver = None
        self.song = None
        self.link = None

    def start_driver(self):
        self.driver = webdriver.Firefox(executable_path=self.gecko_path)

    def window_handle(self):
        # TODO: [Fix] When closed and music changes -> selenium.common.exceptions.WebDriverException: Message: Failed to
        #  decode response from marionette
        try:
            self.wh = self.driver.window_handles
            self.state['running'] = True
        except selenium.common.exceptions.InvalidSessionIdException \
               or selenium.common.exceptions.WebDriverException as session:
            self.state['running'] = False
            self.state['error'] = session

    def search(self, *song):
        if song:
            self.song = song
        try:
            self.driver.get(self.url)
            elem = self.driver.find_element_by_name('q')
            elem.send_keys(self.song)
            elem.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10)
            time.sleep(6)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            top_song = soup.find('div', {'class': 'u-quarter_vertical_margins u-clickable'})
            link = top_song.find('a', {'class': 'mini_card'})
            self.link = link['href']
            return link['href']
        except AttributeError:
            raise AttributeError('Driver is closed')

    def browse(self):
        self.driver.get(self.link)
