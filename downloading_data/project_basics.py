##CSV file headers

import csv

filename = 'downloading_data/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

###Printing the headers and their positions

import csv

filename = 'downloading_data/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

###Extracting and Reading the data
# 
# import csv

# filename = 'downloading_data/data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)

    ##Get high temperatures from this file.
    # high_temps = []
    # for row in reader:
        # high_temp = int(row[5])  ###(index of maximum temperature)
        # high_temps.append(high_temp)
# print(high_temps)
# 
###Plotting Data in a temperature chart
# 
# import csv
# 
# import matplotlib.pyplot as plt
# 
# filename = 'downloading_data/data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)
# 
    ##Get high temperatures from the file
    # high_temps = []
    # for row in reader:
        # high_temp = int(row[5])
        # high_temps.append(high_temp)
# 
##Plot high temperatues
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(high_temps, c='red')
# 
##Format plot
# ax.set_title("Daily high temperatures, July 2018", fontsize=24)
# ax.set_xlabel('', fontsize=16)        ###(we add date to x-label later).
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)
# 
# plt.show()

###Plotting Dates

# import csv
# from datetime import datetime

# import matplotlib.pyplot as plt

# filename = 'downloading_data/data/sitka_weather_07-2018_simple.csv'

# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)

    ###Get Dates, High temperatures from the file
    # dates, high_temps = [], []
    # for row in reader:
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')        ###(index for date is 2 in the row)
        # high_temp = int(row[5])
        # dates.append(current_date)
        # high_temps.append(high_temp)

###Plot dates and high temperatures
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(dates, high_temps, c='red')

###Format plot
# ax.set_title("Daily high temperatures, July 2018", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# figure.autofmt_xdate()      ###(to align dates diagonally)
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()

###Plotting a larger timeframe

# import csv
# from datetime import datetime

# import matplotlib.pyplot as plt

# filename = 'downloading_data/data/sitka_weather_2018_simple.csv'

# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)

    #Get Dates, High temperatures from the file
    # dates, high_temps = [], []
    # for row in reader:
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        # high_temp = int(row[5])
        # dates.append(current_date)
        # high_temps.append(high_temp)

#Plot dates and high temperatures
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(dates, high_temps, c='red')

#Format plot
# ax.set_title("Daily high temperatures - 2018", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# figure.autofmt_xdate()      
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()

###Plotting a Second Data series

# import csv
# from datetime import datetime

# import matplotlib.pyplot as plt

# filename = 'downloading_data/data/sitka_weather_2018_simple.csv'

# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)

    #Get Dates, High and Low temperatures from the file
    # dates, high_temps, low_temps = [], [], []
    # for row in reader:
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        # high_temp = int(row[5])
        # low_temp = int(row[6])
        # dates.append(current_date)
        # high_temps.append(high_temp)
        # low_temps.append(low_temp)

#Plot dates, low and high temperatures
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(dates, high_temps, c='red')
# ax.plot(dates, low_temps, c='blue')

#Format plot
# ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# figure.autofmt_xdate()      
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()

###Shading an Area in the Chart

# import csv
# from datetime import datetime

# import matplotlib.pyplot as plt

# filename = 'downloading_data/data/sitka_weather_2018_simple.csv'

# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)

    #Get Dates, High and Low temperatures from the file
    # dates, high_temps, low_temps = [], [], []
    # for row in reader:
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        # high_temp = int(row[5])
        # low_temp = int(row[6])
        # dates.append(current_date)
        # high_temps.append(high_temp)
        # low_temps.append(low_temp)

#Plot dates, low and high temperatures
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(dates, high_temps, c='red', alpha=0.5)      ###('Alpha' is used to make the color transparent)
# ax.plot(dates, low_temps, c='blue', alpha=0.5)
# ax.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)    

#Format plot
# ax.set_title("Daily high and low temperatures - 2018\n Sitka, Alaska", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# figure.autofmt_xdate()      
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()

###Error Checking and Error handling

# import csv
# filename = 'downloading_data/data/death_valley_2018_simple.csv'      ###(In this file, the high and low temperatures are at indexes 4 and 5. TOBS(at observation time) is included instead of TAVG)
# with open(filename) as f:                           
    # reader = csv.reader(f)      
    # header_row = next(reader)       

    # for index, column_header in enumerate(header_row):
        # print(index, column_header)             

# import csv
# from datetime import datetime

# import matplotlib.pyplot as plt

# filename = 'downloading_data/data/death_valley_2018_simple.csv'     ###(To apply the above 'sitka high low' program for this file, we get an error.)

# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)

    ##Get Dates, High and Low temperatures from the file
    # dates, high_temps, low_temps = [], [], []
    # for row in reader:
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        # high_temp = int(row[4])
        # low_temp = int(row[5])
        # dates.append(current_date)
        # high_temps.append(high_temp)
        # low_temps.append(low_temp)

##Plot dates, low and high temperatures
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(dates, high_temps, c='red', alpha=0.5)     
# ax.plot(dates, low_temps, c='blue', alpha=0.5)
# ax.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)    

##Format plot
# ax.set_title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# figure.autofmt_xdate()      
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()

# import csv
# from datetime import datetime

# import matplotlib.pyplot as plt

# filename = 'downloading_data/data/death_valley_2018_simple.csv'      ###(Exception is used to problem)

# with open(filename) as f:
    # reader = csv.reader(f)
    # header_row = next(reader)

    ##Get Dates, High and Low temperatures from the file
    # dates, high_temps, low_temps = [], [], []
    # for row in reader:
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')  
        # try:
            # high_temp = int(row[4])
            # low_temp = int(row[5])
        # except ValueError:
            # print(f"Missing data for {current_date}")
        # else:
            # dates.append(current_date)
            # high_temps.append(high_temp)
            # low_temps.append(low_temp)

##Plot dates, low and high temperatures
# plt.style.use('seaborn')
# figure, ax = plt.subplots()
# ax.plot(dates, high_temps, c='red', alpha=0.5)     
# ax.plot(dates, low_temps, c='blue', alpha=0.5)
# ax.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)    

##Format plot
# ax.set_title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=22)
# ax.set_xlabel('', fontsize=16)
# figure.autofmt_xdate()      
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()

###Mapping Global Datasets : JSON format

###Explore the structure of the data.
# import json
# filename = 'downloading_data/data/eq_data_1_day_m1.json'
# with open(filename) as f:
    # all_eq_data = json.load(f)

# readable_file = 'downloading_data/data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
    # json.dump(all_eq_data, f, indent=4)

###Making a list of all Earthquakes
# 
# import json
# 
# filename = 'downloading_data/data/eq_data_1_day_m1.json'
# with open(filename) as f:
    # all_eq_data = json.load(f)
# all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))          ###(158 earthquakes)
# 
###Extracting magnitudes
# import json

# filename = 'downloading_data/data/eq_data_1_day_m1.json'
# with open(filename) as f:
    # all_eq_data = json.load(f)
# all_eq_dicts = all_eq_data['features']

# mags = []
# for eq_dict in all_eq_dicts:
    # mag = eq_dict['properties']['mag']
    # mags.append(mag)
# print(mags[:10])

###Extracting Location Data
# import json

# filename = 'downloading_data/data/eq_data_1_day_m1.json'
# with open(filename) as f:
    # all_eq_data = json.load(f)
# all_eq_dicts = all_eq_data['features']

# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
    # mag = eq_dict['properties']['mag']
    # lon = eq_dict['geometry']['coordinates'][0]
    # lat = eq_dict['geometry']['coordinates'][1]
    # mags.append(mag)
    # lons.append(lon)
    # lats.append(lat)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

##Building a world map

# import json
# from plotly.graph_objs import Scattergeo, Layout
# from plotly import offline

# filename = 'downloading_data/data/eq_data_1_day_m1.json'
# with open(filename) as f:
    # all_eq_data = json.load(f)
# all_eq_dicts = all_eq_data['features']

# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
    # mag = eq_dict['properties']['mag']
    # lon = eq_dict['geometry']['coordinates'][0]
    # lat = eq_dict['geometry']['coordinates'][1]
    # mags.append(mag)
    # lons.append(lon)
    # lats.append(lat)

##Map earthquakes
# data = [Scattergeo(lon=lons, lat=lats)]
# layout = Layout(title='Global Earthquakes')

# fig = {'data': data, 'layout':layout}
# offline.plot(fig, filename='global_earthquakes.html')

###Customizing 'data' list and marker size
 
# import json
# from plotly.graph_objs import Scattergeo, Layout
# from plotly import offline
# filename = 'downloading_data/data/eq_data_1_day_m1.json'
# with open(filename) as f:
    # all_eq_data = json.load(f)
# all_eq_dicts = all_eq_data['features']
# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
    # mag = eq_dict['properties']['mag']
    # lon = eq_dict['geometry']['coordinates'][0]
    # lat = eq_dict['geometry']['coordinates'][1]
    # mags.append(mag)
    # lons.append(lon)
    # lats.append(lat)
# 
# data = [{
    # 'type' : 'scattergeo',
    # 'lon'  : lons,
    # 'lat' : lats,
    # 'marker' : {
        # 'size' : [5*mag for mag in mags]
    # },
# }]
# layout = Layout(title='Global Earthquakes')
# fig = {'data': data, 'layout':layout}
# offline.plot(fig, filename='global_earthquakes.html')

##Customizing marker colors and hover text

# import json
# from plotly.graph_objs import Scattergeo, Layout
# from plotly import offline
# filename = f"downloading_data/data/eq_data_30_day_m1.json"
# with open(filename) as f:
    # all_eq_data = json.load(f)
# all_eq_dicts = all_eq_data['features']
# mags, lons, lats, hover_texts = [], [], [], []
# for eq_dict in all_eq_dicts:
    # mag = eq_dict['properties']['mag']
    # lon = eq_dict['geometry']['coordinates'][0]
    # lat = eq_dict['geometry']['coordinates'][1]
    # title = eq_dict['properties']['title']
    # mags.append(mag)
    # lons.append(lon)
    # lats.append(lat)
    # hover_texts.append(title)

# data = [{
    # 'type' : 'scattergeo',
    # 'lon'  : lons,
    # 'lat' : lats,
    # 'text' : hover_texts,
    # 'marker' : {
        # 'size' : [5*mag for mag in mags],
        # 'color' : mags,
        # 'colorscale': 'Viridis',
        # 'reversescale' : True ,
        # 'colorbar' : {'title':'Magnitude'}
    # }
# }]
# layout = Layout(title='Global Earthquakes')
# fig = {'data': data, 'layout':layout}
# offline.plot(fig, filename='global_earthquakes.html')

###Other colorscales in plotly

# from plotly import colors

# for key in colors.PLOTLY_SCALES.keys():
    # print(key)