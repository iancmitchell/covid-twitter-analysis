import unittest
from services.csv_writer import CSVWriter
import pathlib

class CSVWriterTest(unittest.TestCase):
    def setUp(self):
        self.client = CSVWriter()

    def test_initialize(self):
        self.assertIsInstance(self.client, CSVWriter)    

    def test_export_list(self):
        columns = ["id", "name", "gender"]
        data = [
            {"id":1, "name":"tim", "gender":"male"},
            {"id":2, "name":"jane", "gender":"female"}
        ]
        location = str(pathlib.Path().absolute().joinpath("../test_files/test.csv"))
        print(location)
        self.client.export_list(location, data, columns)

if __name__ == "__main__":
    unittest.main()        