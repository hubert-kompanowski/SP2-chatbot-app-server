from datetime import datetime, timedelta
today = datetime.today()

source_page = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json/'

json_stats = {"0": {"date": str(today), "cases": 10567, "deaths": 452, "population": 37972812, "cumulative_nr": 743.88749508},
              "1": {"date": str(today - timedelta(days=1)), "cases": 10567, "deaths": 452, "population": 37972812, "cumulative_nr": 743.88749508},
              "2": {"date": str(today - timedelta(days=2)), "cases": 12597, "deaths": 402, "population": 37972812, "cumulative_nr": 743.88749508},
              "3": {"date": str(today - timedelta(days=3)), "cases": 4655, "deaths": 552, "population": 37972812, "cumulative_nr": 743.88749508},
              "4": {"date": str(today - timedelta(days=4)), "cases": 5674, "deaths": 417, "population": 37972812, "cumulative_nr": 743.88749508},
              "5": {"date": str(today - timedelta(days=5)), "cases": 10004, "deaths": 488, "population": 37972812, "cumulative_nr": 743.88749508},
              "6": {"date": str(today - timedelta(days=6)), "cases": 10167, "deaths": 606, "population": 37972812, "cumulative_nr": 743.88749508},}
