import pandas as pd
from py_mini_racer import py_mini_racer
from requests_html import HTMLSession
from script import utility as util

session = HTMLSession()


class ImportData:
    def __init__(self, url):
        self.url = url

    def tracker(self):
        ctx = py_mini_racer.MiniRacer()
        tracker_xpath = "/html/body/script[1]/text()"
        r = session.get(self.url)
        if r.status_code == 200:
            raw_script = r.html.xpath(tracker_xpath)
            function = util.m_func(raw_script)
            data_exe = ctx.execute(function)
            cases_data = pd.DataFrame(data_exe["state"]["cases"])
            return cases_data
        else:
            print("Source Not Working Technical Problem")

    def daily(self):
        r = session.get(self.url, allow_redirects=False)
        if r.status_code == 200:
            api_data = r.json()["Data"]
            util.c_list(api_data)
            return pd.DataFrame(api_data)
        elif r.status_code == 301:
            print("Api Not Working Redirect to https://ddc.moph.go.th/viralpneumonia/")
        else:
            print("Api Not Working Technical Problem")

    def gov(self):
        r = session.get(self.url)
        if r.status_code == 200:
            data_gov = pd.read_excel(r.html.url, engine="openpyxl")
            data_gov = data_gov.loc[:, ~data_gov.columns.str.match("Unnamed")]
            data_gov.province_of_onset = data_gov.province_of_onset.replace(
                "กทม", "กรุงเทพมหานคร"
            )
            data_gov.notification_date = data_gov.notification_date.ffill()
            data_gov.announce_date = data_gov.announce_date.ffill()
            data_gov.no = data_gov.no.apply(int)
            # print(data_gov.dtypes)
            return data_gov
        else:
            print("Source Not Working Technical Issue")

    def away(self):
        r = session.get(self.url)
        if r.status_code == 200:
            away_covid = pd.read_html(r.html.url, encoding="utf-8")
            away_covid_data = away_covid[0]
            new_header = away_covid_data.iloc[0]
            away_covid_data = away_covid_data[1:]
            away_covid_data.columns = new_header
            away_covid_data = away_covid_data.drop(columns=1.0)
            away_covid_data = away_covid_data.dropna(subset=["place_name"])
            away_covid_data = away_covid_data.reset_index(drop=True)
            return away_covid_data
