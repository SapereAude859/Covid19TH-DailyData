import pandas as pd
import datetime


class NewWave:
    def __init__(self, data):
        self.df = data

    def tracker(self):
        self.df["date"] = pd.to_datetime(self.df["date"], format="%Y-%m-%d")
        new_wave_start = self.df["date"] >= "2020-12-17"
        df_new_wave = self.df.loc[new_wave_start]
        df_new_wave = df_new_wave[df_new_wave.status != "sanitized"]
        return df_new_wave

    def cases(self):
        self.df["ConfirmDate"] = pd.to_datetime(
            self.df["ConfirmDate"], format="%Y-%m-%d %H:%M:%S"
        )
        new_wave_start = self.df["ConfirmDate"] >= "2020-12-17"
        df_new_wave = self.df.loc[new_wave_start]
        return df_new_wave
