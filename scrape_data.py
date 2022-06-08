import time
import pandas as pd
import short_story
from tqdm import tqdm


def story_data_to_df():
    """
    takes all of the story urls we've found and saved and extracts the desired data from each story's page
    using the ShortStory class
    :return: a dataframe with all of our stories' info
    """
    urls_df = pd.read_csv('text_urls.csv')
    dict_to_convert = {}
    try:
        for url in tqdm(urls_df['urls']):
            story_data = short_story.ShortStory.from_soup(url)
            dict_to_convert[story_data.story_id] = story_data.to_dict()
            time.sleep(2)
    except Exception as ex:
        print(ex)
        return pd.DataFrame.from_dict(dict_to_convert, orient='index')
    return pd.DataFrame.from_dict(dict_to_convert, orient='index')


if __name__ == "__main__":
    story_data_to_df().to_csv('story_data.csv', index=False)



