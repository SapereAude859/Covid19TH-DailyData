from script.export_data import ExportData as Export, ZipData as Zip
from script.import_data import ImportData as Import

print('===== Initiate Data Extraction Covid-19 Thailand Data From Available Sources =====' + '\n')

endpoints = ['cases', 'timeline', 'area']
url = 'https://data.go.th/dataset/8a956917-436d-4afd-a2d4-59e4dd8e906e/resource/24ac8406-0cf9-4f8e-a55e' \
        '-b53cf6766d1a/download/pm-covid19-adjusted.xlsx'

cases_data = Import('https://covidtracker.5lab.co/').tracker()
Export(cases_data, 'covid-tracker')

for endpoint in endpoints:
    api_data = Import('https://covid19.th-stat.com/api/open/' + endpoint).daily()
    Export(api_data, endpoint)


data_gov = Import(url).gov()
Export(data_gov, 'Data-Gov')
