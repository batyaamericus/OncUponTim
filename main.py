"""
This file scrapes the main page (https://blog.reedsy.com/short-stories/)
INPUTS : None
OUTPUTS: list of urls of the texts
"""

from globals import *
from urllib.request import Request, urlopen
import re
import pandas as pd
from tqdm import tqdm
import time


def get_urls():
    """
    Collects the urls of all the website's short stories under a certain category
    url: https://blog.reedsy.com/short-stories/fiction/page/.
    Returns a list of urls.
    """

    out_urls = []
    urls = [FICTION_SHORT_STORIES_URL + f"{str(page)}" for page in range(2, 1268 + 1)]
    for u in tqdm(urls):
        req = Request(u, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
        time.sleep(2)
        body = urlopen(req).read()
        urllist = re.findall(r"""<\s*a\s*class="no-decoration"\s*href=["']/short-story([^=]+)["']""",
                             body.decode("utf-8"))
        urllist = ['https://blog.reedsy.com/short-story' + x for x in urllist]
        out_urls.append(urllist)

    return list(set([x for xs in out_urls for x in xs]))


if __name__ == "__main__":
    texts_urls = get_urls()
    print('ok')
    url_dict = {'urls': texts_urls}
    df = pd.DataFrame(url_dict)
    df.to_csv('text_urls.csv')
