#!/usr/bin/env python3
import csv
import requests

path = '/home/myke/bards/bardswork/2020-ark/AI/face-recognition-1/dataset-image/'
datasets = ['kukin', 'vizbor', 'vysockij']

for data in datasets:
    with open(f'{path}{data}/images.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if len(row):
                print (i, row)
                p = requests.get(row[0])
                out = open(f"{path}{data}/{i}.jpg", "wb")
                out.write(p.content)
                out.close()

