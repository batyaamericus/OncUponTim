import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
# import nltk
# from nltk.corpus import stopwords
#
# nltk.download('stopwords')
# stops = set(stopwords.words('english'))


class ShortStory:
    def __init__(self, soup, url):
        '''
        Initialize the ShortStory object.
        :param soup: BeautifulSoup object
        :param url: URL of the story
        collect number of likes, and number of comments, if won contest, which contest won, author, number of author
        submissions, story text, sensitive content tag?, if author responds to comments
        '''
        self.url = url
        self.soup = soup
        self.story_str = self.soup.find(class_='content').get_text()
        self.author = self.soup.find(class_='titre d-block d-xl-none').get_text()
        self.title = self.soup.find(class_='pb-3').get_text()
        self.labels = self.soup.find(class_='content-tag').get_text().split()
        self.likes = int(self.soup.find(class_='oeuvre-fiche-likes oeuvre-fiche-box').get_text()[0])
        self.comments = int(self.soup.find(class_='nb-com').get_text().split()[0])
        self.author_url = self.url.split('/en/story/')[0] + self.soup.find(class_='titre d-block d-xl-none').find('a').get('href')
        # add functions to get words, number of words, unique words, unique words percent, number of sentences, etc

    @staticmethod
    def from_soup(url):
        """
        Get the story's info and turn into soup object.
        Create an ShortStory object from the soup object.
        """
        req = Request('https://blog.reedsy.com/short-story/7wygpy/', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        return ShortStory(soup, url)

