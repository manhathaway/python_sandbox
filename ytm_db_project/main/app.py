from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    json_file = open('listening-history.json', encoding="utf8")
    json_data = json.load(json_file)
            
    return render_template('index.html',
    # json_data = sorted(json_data, key=lambda k : k['timestamp']['date'], reverse=True)
    json_data = json_data
    )

if __name__ == "__main__":
    app.run(debug = True)