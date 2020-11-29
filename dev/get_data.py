from requests import get
from datetime import datetime, timedelta
import json

from config import source_page


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_poland_stats_for_today(page):
    response = get(page, headers={"content-type": "application/json"})
    data = response.json()
    today = datetime.today()
    today = today.strftime('%d/%m/%Y')
    for record in data['records']:
        if record['countriesAndTerritories'] == 'Poland' and record['dateRep'] == today:
            cases = record['cases']
            deaths = record['deaths']
            population = record['popData2019']
            cumulative = record['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000']
            dic = {'date': today, 'cases': cases, 'deaths': deaths, 'population': population,
                   'cumulative_nr': cumulative}
            json_dic = json.dumps(dic)
            return json_dic


def get_stats_last_7_days(page):
    response = get(page, headers={"content-type": "application/json"})
    data = response.json()
    today = datetime.today()
    dic = {}
    count = 0
    for record in data['records']:
        if record['countriesAndTerritories'] == 'Poland' and record['dateRep']:
            date_time = datetime(int(record['year']), int(record['month']), int(record['day']))
            if today >= date_time >= (today - timedelta(days=7)):
                date = record['dateRep']
                cases = record['cases']
                deaths = record['deaths']
                population = record['popData2019']
                cumulative = record['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000']
                dic_tmp = {'date': date, 'cases': cases, 'deaths': deaths, 'population': population,
                           'cumulative_nr': cumulative}
                dic[count] = dic_tmp
                count += 1
                continue
    json_dic = json.dumps(dic)
    return json_dic


if __name__ == '__main__':
    print(get_stats_last_7_days(source_page))
    print(get_poland_stats_for_today(source_page))
