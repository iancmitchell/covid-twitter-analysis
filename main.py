from services.csv_writer import CSVWriter
from twitter_client import TwitterClient
import pathlib

def main():
    client = TwitterClient()
    data = client.search_hashtag("mask")
    writer = CSVWriter()
    columns = data[0].keys()
    location = str(pathlib.Path().absolute().joinpath("test_files/tweets.csv"))
    writer.export_list(location, data, columns)

if __name__ == "__main__":
    main()    