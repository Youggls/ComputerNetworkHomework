import csv
import matplotlib.pyplot as plt

RTT_data_file = open('./data.csv', 'r', encoding='utf8')
RTT_data_file_reader = csv.reader(RTT_data_file)

index = 0
for line in RTT_data_file_reader:
    if index >= 2:
        line[4] = RTT_data_file_reader[index - 1][4] * 0.875 + line[3] * 0.125
    index = index + 1
