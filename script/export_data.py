import os
from rich.console import Console
from tabulate import tabulate
from pathlib import Path
import zipfile

dataset_path = Path()
extensions = ["csv", "xlsx", "json"]
console = Console(color_system="256")


class ExportData:
    def __init__(self, data, name, path):
        self.df = data
        self.name = name
        self.path = path
        self.print_recent()
        self.all_type()
        console.print(
            ">> File Name " + self.name + ".*" + " Successful" + "\n",
            style="green on red",
        )

    def print_recent(self):
        console.print("> File Name " + self.name + ".*" + "\n", style="green on black")
        console.print(
            tabulate(self.df.tail(), headers="keys", showindex=False, tablefmt="grid"),
            overflow="ignore",
            crop=False,
            style="color(5)",
        )

    def all_type(self):
        for extension in extensions:
            path = dataset_path / self.path / extension
            filename = f"{self.name}.{extension}"
            path.parent.mkdir(exist_ok=True)
            if extension == "csv":
                path.mkdir(exist_ok=True)
                self.df.to_csv(
                    f"{path}/{filename}", index=False, header=True, encoding="utf-8"
                )
            if extension == "xlsx":
                path.mkdir(exist_ok=True)
                self.df.to_excel(
                    f"{path}/{filename}",
                    sheet_name=self.name,
                    index=False,
                    header=True,
                    encoding="utf-8",
                    engine="xlsxwriter",
                )
            if extension == "json":
                path.mkdir(exist_ok=True)
                self.df.to_json(f"{path}/{filename}", orient="records")


class ZipData:
    def __init__(self, path):
        self.path = path
        self.dir_name = dataset_path / self.path
        self.file_paths = []
        self.zip()
        console.print(
            ">>> Export Data and Zip " + self.path + " Successful",
            style="blue on black",
        )

    def get_file_path(self):
        for root, files in os.walk(self.dir_name):
            for filename in files:
                file_path = os.path.join(root, filename)
                self.file_paths.append(file_path)
        return self.file_paths

    def zip(self):
        zip_file = zipfile.ZipFile(f"{self.dir_name}.zip", "w")
        with zip_file:
            for file in self.get_file_path():
                zip_file.write(file)
