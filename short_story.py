import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
from tqdm import tqdm
# import nltk
# from nltk.corpus import stopwords
#
# nltk.download('stopwords')
# stops = set(stopwords.words('english'))


class ShortStory:
    def __init__(self, soup):
        '''
        Initialize the ShortStory object.
        :param soup: BeautifulSoup object
        collect number of num_likes, and number of num_comments, if won contest, which contest won, author, number of author
        submissions, story text, sensitive content tag?, if author responds to num_comments
        '''
        self.soup = soup
        self.title = self.soup.title.string.split('by ')[0].split(' –')[0]
        self.author = self.soup.title.string.split('by ')[1].split(r' –')[0]
        # self.categories = self.soup.find(class_='content-tag').get_text().split()
        # self.num_likes = int(self.soup.find(class_='oeuvre-fiche-num_likes oeuvre-fiche-box').get_text()[0])
        # self.num_comments = int(self.soup.find(class_='nb-com').get_text().split()[0])
        # self.story_str = self.soup.find(class_='content').get_text()

        # add functions to get words, number of words, unique words, unique words percent, number of sentences, etc

    @staticmethod
    def from_soup(url):
        """
        Get the story's info and turn into soup object.
        Create an ShortStory object from the soup object.
        """
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        return ShortStory(soup)

    def to_dict(self):
        """
        Return the story's info in a dictionary.
        """
        return {'title': self.title, 'author': self.author}
        # , 'author_url': self.author_url, 'story_str': self.story_str,
        #         'num_likes': self.num_likes, 'num_comments': self.num_comments, 'categories': self.categories}


def scrape_pages():
    # import urls from csv
    df = pd.read_csv("text_urls.csv")
    urls = df.urls.tolist()

    # create instances / scrape
    for url in tqdm(urls):
        ShortStory.from_soup(url)
