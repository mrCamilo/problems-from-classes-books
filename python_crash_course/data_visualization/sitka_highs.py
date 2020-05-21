import csv

import matplotlib.pyplot as mplpp

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print (header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # High temperatures
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    #Low temperatures
    #lows = []
    #for row in reader:
        #   low = int(row[6])
        #  lows.append(low)

    #plot
    mplpp.style.use('seaborn')
    fig, ax = mplpp.subplots()
    ax.plot(highs, c='red')

    #plot format
    mplpp.title("Daily highs, July 2018", fontsize=24)
    mplpp.xlabel('', fontsize=16)
    mplpp.ylabel("Temperature (F)", fontsize=16)
    mplpp.tick_params(axis='both', which='major', labelsize=16)

mplpp.show()

#print(highs)
