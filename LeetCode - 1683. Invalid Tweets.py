# 2024-12-16

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    content_lengths = tweets['content'].str.len()

    return tweets[content_lengths > 15][['tweet_id']]