from requests import get
from datetime import datetime, timedelta
import json

from config import source_page, json_stats, source


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_poland_stats_time(page):
    response = get(page, headers={"content-type": "application/json"})
    data = response.json()
    today = datetime.today()
    dic = {}
    for record in data['records']:
        if record['countriesAndTerritories'] == 'Poland':
            date_time = datetime.strptime(record['dateRep'], '%d/%m/%Y')
            if today >= date_time >= (today - timedelta(days=14)):
                dic['deaths_total'] = record['deaths_weekly']
                dic['cases_total'] = record['cases_weekly']
                dic['rate'] = record['notification_rate_per_100000_population_14-days']
    json_dic = json.dumps(dic)
    return json_dic


def get_stats_last_7_days(page,):
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


def get_stats_last_7_days_new(page1, page2):
    response_first = get(page1, headers={"content-type": "application/json"})
    data = response_first.json()
    today = datetime.today()
    rate = 0
    for record in data['records']:
        if record['countriesAndTerritories'] == 'Poland':
            date_time = datetime.strptime(record['dateRep'], '%d/%m/%Y')
            if today >= date_time >= (today - timedelta(days=14)):
                rate = float(record['notification_rate_per_100000_population_14-days'])

    response = get(page2, headers={"content-type": "application/json"})
    data = response.json()

    lent = len(data)
    minus0 = data[lent-1]['infectedByRegion'][0]
    cases_today = minus0['infectedCount']
    deaths_today = minus0['deceasedCount']

    minus1 = data[lent-2]['infectedByRegion'][0]
    cases_1 = minus1['infectedCount']
    deaths_1 = minus1['deceasedCount']

    minus2 = data[lent - 3]['infectedByRegion'][0]
    cases_2 = minus2['infectedCount']
    deaths_2 = minus2['deceasedCount']

    minus3 = data[lent - 4]['infectedByRegion'][0]
    cases_3 = minus3['infectedCount']
    deaths_3 = minus3['deceasedCount']

    minus4 = data[lent - 5]['infectedByRegion'][0]
    cases_4 = minus4['infectedCount']
    deaths_4 = minus4['deceasedCount']

    minus5 = data[lent - 6]['infectedByRegion'][0]
    cases_5 = minus5['infectedCount']
    deaths_5 = minus5['deceasedCount']

    minus6 = data[lent - 7]['infectedByRegion'][0]
    cases_6 = minus6['infectedCount']
    deaths_6 = minus6['deceasedCount']

    today = datetime.today()

    stats = {"stats": [{"date": str(today), "cases": cases_today, "deaths": deaths_today,
                          "population": 37972812,
                          "cumulative_nr": rate},
                         {"date": str(today - timedelta(days=1)),
                          "cases": cases_1,
                          "deaths": deaths_1, "population": 37972812,
                          "cumulative_nr": rate},
                         {"date": str(today - timedelta(days=2)),
                          "cases": cases_2,
                          "deaths": deaths_2, "population": 37972812,
                          "cumulative_nr": rate},
                         {"date": str(today - timedelta(days=3)), "cases": cases_3,
                          "deaths": deaths_3, "population": 37972812,
                          "cumulative_nr": rate},
                         {"date": str(today - timedelta(days=4)), "cases": cases_4,
                          "deaths": deaths_4, "population": 37972812,
                          "cumulative_nr": rate},
                         {"date": str(today - timedelta(days=5)),
                          "cases": cases_5,
                          "deaths": deaths_5, "population": 37972812,
                          "cumulative_nr": rate},
                         {"date": str(today - timedelta(days=6)),
                          "cases": cases_6,
                          "deaths": deaths_6, "population": 37972812,
                          "cumulative_nr": rate}], }

    return stats


if __name__ == '__main__':
    print(get_stats_last_7_days_new(source_page, source))
