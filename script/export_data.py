import os
import pandas as pd
from pathlib import Path
import zipfile

dataset_path = Path()
extensions = ['csv', 'xlsx', 'json']


class ExportData:
    def __init__(self, data, name):
        try:
            self.df = pd.DataFrame(data)
            self.name = name
            self.all_type()
        except ValueError:
            self.df = pd.read_excel(data, engine='openpyxl')
            self.name = name
            self.all_type()

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


class ZipData:
    def __init__(self):
        self.dir_name = dataset_path / 'dataset'
        self.file_paths = []
        self.zip()

    def get_file_path(self):
        for root, directories, files in os.walk(self.dir_name):
            for filename in files:
                file_path = os.path.join(root, filename)
                self.file_paths.append(file_path)
        return self.file_paths

    def zip(self):
        zip_file = zipfile.ZipFile(f'{self.dir_name}.zip', 'w')
        with zip_file:
            for file in self.get_file_path():
                zip_file.write(file)
