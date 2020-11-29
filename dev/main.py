from flask import Flask

from config import source_page
from dev.get_data import get_poland_stats_for_today, get_stats_last_7_days

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to covid stats'


@app.route('/today', methods=['GET'])
def today_stats():
    return get_poland_stats_for_today(source_page)


@app.route('/stats', methods=['GET'])
def stats():
    return get_stats_last_7_days(source_page)


if __name__ == '__main__':
    app.run(threaded=True, port=8080, debug=True)
