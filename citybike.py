import requests
import pandas as pd
import matplotlib.pyplot as plt

r = requests.get('http://www.citibikenyc.com/stations/json')

key_list = [] #unique list of keys for each station listing
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)
            
print key_list


df = pd.io.json.json_normalize(r.json()['stationBeanList'])

print df

df['availableBikes'].hist()
plt.savefig("available.png")

plt.clf()

df['totalDocks'].hist()
plt.savefig("totalDocks.png")