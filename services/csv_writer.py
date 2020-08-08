import csv 
from typing import List, Dict
import re

class Dataframe(object):
    def __init__(self, columns: List, data: List[Dict]):
        self.columns = columns
        self.data = data

class CSVWriter(object):
    def _verify_location(self, location: str):
        if not re.search(".csv$", location):
            raise SyntaxError(f"Location must end in .csv. Current location: {location}")

    def export_list(self, location: str, data: List, columns: List):
        self._verify_location(location)
        with open(location, "w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(columns)
            for line in data:
                row = [line.get(column) for column in columns]
                writer.writerow(row)

    def import_csv(self, location: str) -> Dataframe:
        self._verify_location(location)
        with open(location, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            columns = []
            data = []
            read_columns = True
            for row in reader:
                if read_columns:
                    columns = row
                    read_columns = False
                else:
                    row_dict = {}
                    for i in range(len(columns)):
                        row_dict[columns[i]] = row[i]
                    data.append(row_dict)
            return Dataframe(columns, data)        
            
