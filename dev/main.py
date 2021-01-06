from flask import Flask

from config import source_page, source
from dev.get_data import get_poland_stats_time, get_stats_last_7_days_new

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to covid stats'


@app.route('/time_charts', methods=['GET'])
def today_stats():
    return get_poland_stats_time(source_page)


@app.route('/stats', methods=['GET'])
def stats():
    return get_stats_last_7_days_new(source_page, source)


if __name__ == '__main__':
    app.run(threaded=True, port=8080, debug=True)
