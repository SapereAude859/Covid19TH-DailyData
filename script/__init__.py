from script.export_data import ExportData as Export, ZipData as Zip
from script.import_data import ImportData as Import
from script.week_analyze import WeekAnalyze as Week

print('===== Initiate Data Extraction Covid-19 Thailand Data From Available Sources =====' + '\n')

endpoints = ['cases', 'timeline', 'area']
url = 'https://data.go.th/dataset/8a956917-436d-4afd-a2d4-59e4dd8e906e/resource/24ac8406-0cf9-4f8e-a55e' \
        '-b53cf6766d1a/download/pm-covid19-adjusted.xlsx'

cases_data = Import('https://covidtracker.5lab.co/').tracker()
Export(cases_data, 'covid-tracker', 'dataset')
cases_data_week = Week(cases_data).tracker()
Export(cases_data_week, 'covid-tracker-week', 'RecentWeekAlert_Data🔥')


for endpoint in endpoints:
    if endpoint == 'cases':
        api_data = Import('https://covid19.th-stat.com/api/open/' + endpoint).daily()
        Export(api_data, endpoint, 'dataset')
        cases_api_week = Week(api_data).cases()
        Export(cases_api_week, 'cases_week', 'RecentWeekAlert_Data🔥')
    else:
        api_data = Import('https://covid19.th-stat.com/api/open/' + endpoint).daily()
        Export(api_data, endpoint, 'dataset')


data_gov = Import(url).gov()
Export(data_gov, 'Data-Gov', 'dataset')
data_gov_week = Week(data_gov).gov()
Export(data_gov_week, 'data-gov-week', 'RecentWeekAlert_Data🔥')


Zip('dataset')
Zip('RecentWeekAlert_Data🔥')
