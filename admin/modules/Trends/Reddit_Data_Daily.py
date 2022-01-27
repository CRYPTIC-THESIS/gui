import pandas as pd
from pmaw import PushshiftAPI
import datetime as dt

def scrape_reddit_data(b_y,b_m,b_d,a_y,a_m,a_d):
    before = int(dt.datetime(b_y,b_m,b_d,0,0).timestamp())
    after = int(dt.datetime(a_y,a_m,a_d,0,0).timestamp())
    api = PushshiftAPI()

    keyword = ['btc','eth','doge','bitcoin','ethereum','dogecoin']

    def crawler(key):
        query = api.search_submissions(q=key, before=before, after=after)
        print(f'Retrieved {len(query)} posts from Pushshift')

        query_df = pd.DataFrame(query)

        query_df.to_csv('"C:/Users/TUF GAMING A15/Documents/Thesis/DATA/reddit_'+key+'_'+str(after)+'_to_'+str(before)+'.csv', header=True, index=False, columns=list(query_df.axes[1]))

        query_df = query_df.iloc[0:0]