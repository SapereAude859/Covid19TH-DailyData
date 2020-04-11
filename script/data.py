from py_mini_racer import py_mini_racer
from requests_html import HTMLSession
from script import utility as util
from script.export_data import ExportData as Export, ZipData as Zip

session = HTMLSession()


def covid_tracker():
    ctx = py_mini_racer.MiniRacer()
    tracker_xpath = '/html/body/script[1]/text()'
    r = session.get('https://covidtracker.5lab.co/')
    if r.status_code == 200:
        raw_script = r.html.xpath(tracker_xpath)
        function = util.m_func(raw_script)
        data_exe = ctx.execute(function)
        cases_data = data_exe['state']['cases']
        Export(cases_data, 'covid-tracker')
        print('Extract Covid-Tracker Successful')


def covid_daily():
    url = 'https://covid19.th-stat.com/api/open/'
    endpoints = ['cases', 'timeline', 'area']
    for endpoint in endpoints:
        r = session.get(url + endpoint)
        if r.status_code == 200:
            api_data = r.json()['Data']
            util.c_list(api_data)
            Export(api_data, endpoint)
            print('Extract ', endpoint, ' Successful')


def run():
    print('Initiate Data Extraction')
    covid_tracker()
    covid_daily()
    Zip()
    print('Export Data and Zip Successful')
