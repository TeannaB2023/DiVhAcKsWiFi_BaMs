import csv

class Location:
    def __init__(self, z, lon, lat):
        self.zip = z 
        self.longitude = lon
        self.latitude = lat
l1 = Location(10001,32.2,4.5)

List = []

with open(Sample CSV file - Sheet1.csv, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile)