from requests import get
from datetime import datetime, timedelta
import json

from config import source_page, json_stats


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_poland_stats_time(page):
    response = get(page, headers={"content-type": "application/json"})
    data = response.json()
    today = datetime.today()
    cases_7 = 0
    deaths_7 = 0
    dic = {}
    count = 0
    for record in data['records']:
        if record['countriesAndTerritories'] == 'Poland':
            date_time = datetime.strptime(record['dateRep'], '%d/%m/%Y')
            if today >= date_time >= (today - timedelta(days=7)):
                dic['deaths_total'] = record['deaths_weekly']
                dic['cases_total'] = record['cases_weekly']
    json_dic = json.dumps(dic)
    json_ok = {**json_dic, **json_stats}
    return json_ok


def get_stats_last_7_days(page):
    response = get(page, headers={"content-type": "application/json"})
    data = response.json()
    today = datetime.today()
    dic = {}
    count = 0
    for record in data['records']:
        if record['countriesAndTerritories'] == 'Poland ':
            #date_time = datetime.strptime(record['dateRep'], '%d/%m/%Y')
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
    return json_stats


if __name__ == '__main__':
    print(get_poland_stats_time(source_page))
