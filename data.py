import json_lines
import matplotlib.pyplot as plt

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
        tmp_timeline.append(i['data'])
    return tmp_value, tmp_timeline
    
    
# Plot the charts
plt.subplot(2, 2, 1)
plt.plot(makeChart(eur_pln)[1], makeChart(eur_pln)[0], color='r', label='eur_pln')
# plt.savefig('eur_pln.png')

plt.subplot(2, 2, 2)
plt.plot(makeChart(usd_pln)[1], makeChart(usd_pln)[0], color='g', label='usd_pln')
# plt.savefig('usd_pln.png')

plt.subplot(2, 2, 3)
plt.plot(makeChart(eur_usd)[1], makeChart(eur_usd)[0], color='b', label='eur_usd')
# plt.savefig('eur_usd.png')

plt.legend()
plt.show()
