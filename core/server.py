from flask import jsonify
from datetime import datetime
from core import app

from core.apis.tweet_search import tweet_scrape_resources




app.register_blueprint(tweet_scrape_resources, url_prefix='/twitter')


@app.route('/')
def ready():
    response = jsonify({
        'status': 'ready',
        'time': datetime.now()
    })

    return response

if __name__ == '__main__' :
    app.run(debug=True)


