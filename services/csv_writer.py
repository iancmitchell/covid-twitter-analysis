import csv 
from typing import List
import re

class CSVWriter(object):
    def export_list(self, location: str, data: List, columns: List):
        if not re.search(".csv$", location):
            raise SyntaxError(f"Location must end in .csv. Current location: {location}")
        with open(location, "w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(columns)
            for line in data:
                row = [line.get(column) for column in columns]
                writer.writerow(row)