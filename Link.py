import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Link:
    def __init__(self, song, path):
        """

        :type song: str
        :type path: raw str
        """
        self.url = "https://genius.com/"
        self.song = song
        self.gecko_path = path
        self.driver = webdriver.Firefox(executable_path=self.gecko_path)

    def search(self):
        driver = self.driver
        driver.get(self.url)
        elem = driver.find_element_by_name("q")
        elem.send_keys(self.song)
        elem.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10)
        time.sleep(4)
        assert "No results found." not in driver.page_source
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            top_song = soup.find('div', {'class': 'u-quarter_vertical_margins u-clickable'})
            item = top_song.find('a', {'class': 'mini_card'})
            return item["href"]
        except AttributeError:
            driver.close()
            return AttributeError
        finally:
            driver.close()
