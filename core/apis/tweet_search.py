from flask import Blueprint
from flask import jsonify
from core.apis import client
from core.Models.tweet_search import TweetSearchResult
import pandas as pd 

tweet_scrape_resources = Blueprint('tweet_scrape_resources', __name__)

def ranking(tweet_dict):
    df_list = [pd.DataFrame(dict_)
        for dict_ in tweet_dict]
    df = pd.concat(df_list)
    df.sort_values(by=["b_view_count", "c_no_of_likes", "d_no_of_retweet"], inplace=True, ascending=False)
    sorted_result = []
    for row in df.itertuples(index=False):
        data = {
            'a_tweet_text' : row[0],
            'b_view_count' : row[1], 
            'c_no_of_likes' :row[2],
            'd_no_of_retweet': row[3],
        }
        sorted_result.append(data)
    print(sorted_result[:5])
    return sorted_result


@tweet_scrape_resources.route('/<query>',  methods=['GET'], strict_slashes=False)
def scrape_tweet(query) :
    query_key = query.strip()
    result = TweetSearchResult.get_tweet_by_key(query_key=query_key)
    
    if len(result) > 0:
        result = [{
            'a_tweet_text' : [tweet.tweet_text],
            'b_view_count' : [tweet.view_count],    
            'c_no_of_likes' : [tweet.no_of_likes],
            'd_no_of_retweet' : [tweet.no_of_retweets],
        } for tweet in result] 
        
        response = ranking(result)

        return jsonify({'tweets' : response})

    tweets = client.search_tweet(query, 'Top')
    
    for tweet in tweets:
        data = {
            'a_tweet_text' : [tweet.text.split("https")[0]],
            'b_view_count' : [tweet.view_count],    
            'c_no_of_likes' : [tweet.favorite_count],
            'd_no_of_retweet' : [tweet.retweet_count],
        }
        result.append(data)
        tweet = TweetSearchResult(query_key=query_key, 
                                  no_of_likes=tweet.favorite_count, 
                                  no_of_retweets=tweet.retweet_count,
                                  tweet_text=tweet.text.split("https")[0],
                                  view_count=tweet.view_count)
        tweet.create_tweet()
    result = ranking(result)
    response = jsonify({'tweets' : result})
    return response
