from core import db
from datetime import datetime



class TweetSearchResult(db.Model):

    __tablename__ = 'tweetsearchresult'
    
    id = db.Column(db.Integer,  db.Sequence('tweetsearchresult_id_seq'), primary_key=True)
    search_date = db.Column(db.TIMESTAMP(), default=datetime.now(), nullable =False)
    query_key = db.Column(db.String)
    no_of_likes = db.Column(db.Integer)
    no_of_retweets = db.Column(db.Integer)
    view_count = db.Column(db.Integer)
    tweet_text = db.Column(db.String)

    def __init__(self, query_key, no_of_likes, no_of_retweets, tweet_text, view_count) :
        self.query_key = query_key
        self.no_of_likes = no_of_likes
        self.no_of_retweets = no_of_retweets
        self.tweet_text = tweet_text
        self.view_count = view_count
        self.search_date = datetime.now()
    
    def create_tweet(self):
        print(self.tweet_text)
        db.session.add(self)
        db.session.commit()
        db.session.flush()
    
    @classmethod
    def get_tweet_by_key(cls, query_key) :
        return cls.query.filter_by(query_key=query_key).all()
