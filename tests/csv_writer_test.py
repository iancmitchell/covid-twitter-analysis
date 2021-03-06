import unittest
from services.csv_writer import CSVWriter, Dataframe
import pathlib

class CSVWriterTest(unittest.TestCase):
    def setUp(self):
        self.client = CSVWriter()

    def test_initialize(self):
        self.assertIsInstance(self.client, CSVWriter)    

    def test_export_list(self):
        columns = ["id", "name", "gender"]
        data = [
            {"id":"1", "name":"tim", "gender":"male"},
            {"id":"2", "name":"jane", "gender":"female"}
        ]
        location = str(pathlib.Path().absolute().joinpath("../test_files/test.csv"))
        print(location)
        self.client.export_list(location, data, columns)
        test_dataframe = self.client.import_csv(location)
        self.assertIsInstance(test_dataframe, Dataframe)
        self.assertListEqual(test_dataframe.columns, columns)
        self.assertListEqual(test_dataframe.data, data)

if __name__ == "__main__":
    unittest.main()        