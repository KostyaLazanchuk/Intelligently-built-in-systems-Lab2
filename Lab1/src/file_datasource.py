from csv import reader
from datetime import datetime
from domain.aggregated_data import AggregatedData
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from typing import List
import config

class FileDatasource:
    def __init__(self, accelerometer_filename: str, gps_filename: str) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        pass

    def file_data_reader(self, path: str):
        while True:
            file = open(path)
            data_reader = reader(file)
            header = next(data_reader)

            for row in data_reader:
                yield row

            file.close()

    def read(self) -> AggregatedData:
        dataList = []
        for i in range(5):
            dataList.append(
                AggregatedData(
                    Accelerometer(*next(self.accelerometer_data_reader)),
                    Gps(*next(self.gps_data_reader)),
                    datetime.now(),
                    config.USER_ID,
                )
            )

        return dataList

    def startReading(self, *args, **kwargs):
        self.accelerometer_data_reader = self.file_data_reader(self.accelerometer_filename)
        self.gps_data_reader = self.file_data_reader(self.gps_filename)

    def stopReading(self, *args, **kwargs):
        pass