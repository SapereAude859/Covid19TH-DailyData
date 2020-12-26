import pandas as pd
import datetime
from pathlib import Path

week_path = Path()
extensions = ["csv", "xlsx", "json"]


# Get 14 Days Recent Result
class WeekAnalyze:
    def __init__(self, data):
        self.df = data

    def tracker(self):
        self.df["date"] = pd.to_datetime(self.df["date"], format="%Y-%m-%d")
        df_week = self.df[
            self.df.date > datetime.datetime.now() - pd.to_timedelta("14day")
        ]
        return df_week

    def cases(self):
        self.df["ConfirmDate"] = pd.to_datetime(
            self.df["ConfirmDate"], format="%Y-%m-%d %H:%M:%S"
        )
        df_week = self.df[
            self.df.ConfirmDate > datetime.datetime.now() - pd.to_timedelta("14day")
        ]
        return df_week

    def gov(self):
        self.df["notification_date"] = pd.to_datetime(
            self.df["notification_date"], format="%Y-%m-%d"
        )
        df_week = self.df[
            self.df.notification_date
            > datetime.datetime.now() - pd.to_timedelta("14day")
        ]
        return df_week
