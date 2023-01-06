import json_lines
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime

eur_pln, usd_pln, eur_usd  = [], [], []

# Get the data from API
with open('./data/currency.jl', 'rb') as data_file:
    for item in json_lines.reader(data_file):
        if item['title'] == 'EUR/PLN':
            eur_pln.append(item)
        elif item['title'] == 'EUR/USD':
            eur_usd.append(item)
        elif item['title'] == 'USD/PLN':
            usd_pln.append(item)
              
def makeChart(tmp):
    tmp_value, tmp_timeline = [], []
    for i in tmp:
        curr_value = float(i['value'].strip().replace(",", "."))
        tmp_value.append(curr_value)
        tmp_timeline.append(datetime.strptime(i['data'], '%Y-%m-%d'))
        
    return tmp_value, tmp_timeline
    
# Plot the charts
plt.plot(makeChart(eur_pln)[1], makeChart(eur_pln)[0], color='r', label='eur_pln')
plt.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
plt.legend()
plt.title('EUR/PLN')
plt.savefig('eur_pln.png')
plt.show()

plt.plot(makeChart(usd_pln)[1], makeChart(usd_pln)[0], color='g', label='usd_pln')
plt.legend()
plt.title('USD/PLN')
plt.savefig('usd_pln.png')
plt.show()

plt.plot(makeChart(eur_usd)[1], makeChart(eur_usd)[0], color='b', label='eur_usd')
plt.legend()
plt.title('EUR/USD')
plt.savefig('eur_usd.png')
plt.show()




