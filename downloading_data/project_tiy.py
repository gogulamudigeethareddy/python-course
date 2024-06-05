###Sitka Rainfall
# 
# import csv
# from datetime import datetime
# import matplotlib.pyplot as plt
# 
# filename = 'data/sitka_weather_2018_simple.csv'
# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)
# 
    #for index, column_name in enumerate(header_row):
       # print(index, column_name)
    # 
    # dates = []
    # precipitation = []
    # for row in reader:
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        # dates.append(current_date)
        # precipitation_value = float(row[3])
        # precipitation.append(precipitation_value)
    # 
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(dates, precipitation, c='green')     
# 
##Format plot
# ax.set_title("Precipitation in 2018 - Sitka, Alaska", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# figure.autofmt_xdate()      
# ax.set_ylabel("Precipiation", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)
# 
# plt.show()

###Death_valley Rainfall

# import csv
# from datetime import datetime
# import matplotlib.pyplot as plt

# filename = 'data/death_valley_2018_simple.csv'
# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)
    # 
    # dates = []
    # precipitation = []
    # for row in reader:
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        # dates.append(current_date)
        # precipitation_value = float(row[3])
        # precipitation.append(precipitation_value)
    # 
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(dates, precipitation, c='green')     

##Format plot
# ax.set_title("Precipitation in 2018 - Death valley, CA", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# figure.autofmt_xdate()      
# ax.set_ylabel("Precipiation", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename1 = 'data/death_valley_2018_simple.csv'      
filename2 = 'data/sitka_weather_2018_simple.csv'

with open(filename1) as f1:
    reader_1 = csv.reader(f1)
    header_row1 = next(reader_1)

    ###Get Dates, High and Low temperatures from the file
    dates1, high_temps1, low_temps1 = [], [], []
    for row in reader_1:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        try:
            high_temp1 = int(row[4])
            low_temp1 = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates1.append(current_date)
            high_temps1.append(high_temp1)
            low_temps1.append(low_temp1)      

with open(filename2) as f2:
    reader_2 = csv.reader(f2)
    header_row2 = next(reader_2)

    ###Get Dates, High and Low temperatures from the file
    dates2, high_temps2, low_temps2 = [], [], []
    for row in reader_2:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        try:
            high_temp2 = int(row[5])
            low_temp2 = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates2.append(current_date)
            high_temps2.append(high_temp2)
            low_temps2.append(low_temp2)

###Plot dates, low and high temperatures
plt.style.use('seaborn')
fig, (ax1, ax2) = plt.subplots(2, 1, sharey=True, figsize=(8,6))

ax1.plot(dates1, high_temps1, c='red', alpha=0.5)     
ax1.plot(dates1, low_temps1, c='blue', alpha=0.5)
ax1.fill_between(dates1, high_temps1, low_temps1, facecolor='blue', alpha=0.1)

ax2.plot(dates2, high_temps2, c='red', alpha=0.5)     
ax2.plot(dates2, low_temps2, c='blue', alpha=0.5)
ax2.fill_between(dates2, high_temps2, low_temps2, facecolor='blue', alpha=0.1)    

###Format plot
fig.autofmt_xdate()     

ax1.set_title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=16)
ax1.set_ylabel("Temperature (F)", fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)

ax2.set_title("Daily high and low temperatures - 2018\nSitka, Alaska", fontsize=16)
ax2.set_xlabel('Date', fontsize=12)  
ax2.set_ylabel("Temperature (F)", fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)

plt.show()