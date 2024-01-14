from flask import Flask, render_template
from ytmusicapi import YTMusic
import json
from datetime import date
from datetime import timedelta
import calendar

app = Flask(__name__)

@app.route('/')
def index():
    ytm_api = YTMusic('oauth.json')
    data = ytm_api.get_history()
    
    api_data = []
    
    def timeFormat(data):
        if (data == 'Today'):
            return str(date.today())
        elif (data == 'Yesterday'):
            return str(date.today() - timedelta(days = 1))
        elif (data == 'This week'):
            return str(date.today() - timedelta(days = 2)) + " to " + str(date.today() - timedelta(days = 7))
        elif (data == 'Last week'):
            return str(date.today() - timedelta(days = 8)) + " to " + str(date.today() - timedelta(days = 14))
        else:
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            return str(data.split()[1]) + "-" + str(months.index(data.split()[0][0:3]) + 1)
    
    for i in data:
        if isinstance(i['album'], dict):
            api_data.append({
                "artist": i['artists'][0]['name'],
                "track": i['title'],
                "album": i['album']['name'],
                "thumbnail": i['thumbnails'][0]['url'],
                "time": timeFormat(i['played'])
            })
        else:
            api_data.append({
                "artist": i['artists'][0]['name'],
                "track": i['title'],
                "thumbnail": i['thumbnails'][0]['url'],
                "time": timeFormat(i['played'])
            })
            
    return render_template('index.html',
    api_data = sorted(api_data, key=lambda k : k['time'], reverse=True)
    )

if __name__ == "__main__":
    app.run(debug = True)