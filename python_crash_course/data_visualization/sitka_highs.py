import csv
from datetime import datetime
import matplotlib.pyplot as mplpp

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # High temperatures
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    #Low temperatures
    #lows = []
    #for row in reader:
        #   low = int(row[6])
        #  lows.append(low)

    #plot
    mplpp.style.use('seaborn')
    fig, ax = mplpp.subplots()
    ax.plot(dates, highs, c='red')

    #plot format
    mplpp.title("Daily highs, July 2018", fontsize=24)
    mplpp.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    mplpp.ylabel("Temperature (F)", fontsize=16)
    mplpp.tick_params(axis='both', which='major', labelsize=16)

mplpp.show()

#print(highs)
