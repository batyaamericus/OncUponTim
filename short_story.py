import requests
import bs4


def get_story(url):
    """
    GET the story's info and turn into soup object
    """
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup


class ShortStory:
    def __init__(self, soup, url):
        self.url = url
        self.soup = soup
        self.story_str = self.soup.find(class_='content').get_text()
        self.author = self.soup.find(class_='titre d-block d-xl-none').get_text()
        self.title = self.soup.find(class_='pb-3').get_text()
        self.labels = self.soup.find(class_='content-tag').get_text().split()
        self.reading_time, self.reading_time_units = self.soup.find(class_='oeuvre-fiche-time oeuvre-fiche-box').get_text().split()
        self.num_users_read = int(self.soup.find(class_='oeuvre-fiche-read oeuvre-fiche-box').get_text()[0])
        self.likes = int(self.soup.find(class_='oeuvre-fiche-likes oeuvre-fiche-box').get_text()[0])
        self.comments = int(self.soup.find(class_='nb-com').get_text().split()[0])
        self.author_url = self.url.split('/en/story/')[0] + self.soup.find(class_='titre d-block d-xl-none').find('a').get('href')
        self.story_words = self.story_str.split()
        self.story_words_len = len(self.story_words)
        self.story_words_unique = len(set(self.story_words))
        self.story_words_unique_percent = round(self.story_words_unique / self.story_words_len * 100, 2)

