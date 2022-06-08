from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
# import nltk
# from nltk.corpus import stopwords
#
# nltk.download('stopwords')
# stops = set(stopwords.words('english'))


class ShortStory(object):
    def __init__(self, soup, url):
        '''
        Initialize the ShortStory object.
        :param soup: BeautifulSoup object
        :param url: url that the soup came from
        '''
        self.url = url
        self.story_id = self.url.split('/')[-2]
        self.soup = soup
        self.title = self.soup.title.string.split('by ')[0].split(' –')[0]
        self.author = self.soup.title.string.split('by ')[1].split(r' –')[0]
        # taking the second element of the list created by .split() would give us only the contest number, but
        # supposedly not all stories have been entered into contests and I don't want to get an error
        # so we'll preprocess
        # TODO can pull link to contest from here (NLP)
        self.contest_num = self.soup.find(class_='row-blue-dark').a.string.split()
        if soup.find(class_='row-super-thin row-blue'):
            self.won_contest = [part for part in self.soup.find(class_='row-super-thin row-blue').get_text().split('\n') if part]
        else:
            self.won_contest = None
        self.categories = self.soup.find(class_='small space-top-xs-md').get_text().split()
        likes, comments = [part.split() for part in self.soup.find(class_='text-grey space-top-xs-md').get_text().split('\n') if part and part.split()]
        self.num_likes = int(likes[0])
        self.num_comments = int(comments[0])
        self.story_html = self.soup.find('article')
        pub_date_pattern = '[A-Z][a-z]+ \d{2}, \d{4} \d{2}:\d{2}'
        self.date_published = [re.search(pub_date_pattern, tag.get_text())[0] for tag in soup.find_all(class_='cell-shrink') if re.search(pub_date_pattern, tag.get_text())][0]

    @staticmethod
    def from_soup(url):
        """
        Get the story's info and turn into soup object.
        Create an ShortStory object from the soup object.
        """
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        return ShortStory(soup, url)

    def to_dict(self):
        """
        Return the story's info in a dictionary.
        """
        return self.__dict__