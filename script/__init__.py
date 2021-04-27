from script.export_data import ExportData as Export, ZipData as Zip
from script.import_data import ImportData as Import
from script.week_analyze import WeekAnalyze as Week
from script.new_wave_analyze import NewWave as Wave

print(
    "===== Initiate Data Extraction Covid-19 Thailand Data From Available Sources ====="
    + "\n"
)

endpoints = ["cases", "timeline", "area"]
# url = (
#     "https://data.go.th/dataset/8a956917-436d-4afd-a2d4-59e4dd8e906e/resource/d838f9b0-f8ad-4223-86c7-c380f8589da1"
#     "/download/pm-21-04-64v1.csv "
# )
sheets = ["data", "watchout", "risk", "patient"]
away_url = "https://docs.google.com/spreadsheets/u/0/d/11Gx-Wc2bXb2pAcwKT4jcuLLZ0BYoCrjixo54UxX3KTw/pubhtml"

# ->Covid Tracker Shutdown Services
# cases_data = Import("https://covidtracker.5lab.co/").tracker()
# Export(cases_data, "covid-tracker", "dataset")
# cases_data_week = Week(cases_data).tracker()
# Export(cases_data_week, "covid-tracker-week", "Recent 14Days Alert Data🔥")
# new_wave_tracker = Wave(cases_data).tracker()
# Export(new_wave_tracker, "new-wave-tracker", "New Wave Data🔥")

for endpoint in endpoints:
    if endpoint == "cases":
        api_data = Import("https://covid19.th-stat.com/api/open/" + endpoint).daily()
        Export(api_data, endpoint, "dataset")
        cases_api_week = Week(api_data).cases()
        Export(cases_api_week, "cases_week", "Recent 14Days Alert Data🔥")
        new_wave_cases = Wave(api_data).cases()
        Export(new_wave_cases, "new-wave-cases", "New Wave Data🔥")
        provinces_cases = Wave(api_data).cases_provinces()
        Export(provinces_cases, "provinces-cases", "New Wave Data🔥")
    else:
        api_data = Import("https://covid19.th-stat.com/api/open/" + endpoint).daily()
        Export(api_data, endpoint, "dataset")

# data_gov = Import(url).gov()
# Export(data_gov, "Data-Gov", "dataset")
# try:
#     data_gov_week = Week(data_gov).gov()
#     Export(data_gov_week, "data-gov-week", "Recent 14Days Alert Data🔥")
# except TypeError:
#     pass

away_covid = Import(away_url).away()
Export(away_covid, "away-covid", "dataset")
away_covid_week = Week(away_covid).away()
Export(away_covid_week, "away-covid-week", "Recent 14Days Alert Data🔥")

Zip("dataset")
Zip("Recent 14Days Alert Data🔥")
