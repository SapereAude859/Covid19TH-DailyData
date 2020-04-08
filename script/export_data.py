import pandas as pd
from pathlib import Path

dataset_path = Path()
extensions = ['csv', 'xlsx', 'json']


class ExportData:
    def __init__(self, data, name):
        self.df = pd.DataFrame(data)
        self.name = name

    def all_type(self):
        for extension in extensions:
            path = dataset_path / 'dataset' / extension
            filename = f'{self.name}.{extension}'
            path.parent.mkdir(exist_ok=True)
            if extension == 'csv':
                path.mkdir(exist_ok=True)
                self.df.to_csv(f'{path}/{filename}', index=False, header=True, encoding='utf-8')
            if extension == 'xlsx':
                path.mkdir(exist_ok=True)
                self.df.to_excel(f'{path}/{filename}', sheet_name=self.name, index=False, header=True,
                                 encoding='utf-8',
                                 engine='xlsxwriter')
            if extension == 'json':
                path.mkdir(exist_ok=True)
                self.df.to_json(f'{path}/{filename}', orient='records')
