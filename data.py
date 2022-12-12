import json_lines
import matplotlib.pyplot as plt

eur_pln = []
usd_pln = []
eur_usd = []

with open('env/webspider/currency.jl', 'rb') as data_file:
    for item in json_lines.reader(data_file):
        if item['title'] == 'EUR/PLN':
            eur_pln.append(item)
        elif item['title'] == 'EUR/USD':
            eur_usd.append(item)
        elif item['title'] == 'USD/PLN':
            usd_pln.append(item)
            
# print(eur_usd)
# print(usd_pln)

# Data for plotting for EUR/PLN
# print(eur_pln)
eur_pln_value = []
eur_pln_timeline = []
for i in eur_pln:
    curr_value = float(i['value'].strip().replace(",", "."))
    eur_pln_value.append(curr_value)
    eur_pln_timeline.append(i['data'])
    
# print(eur_pln_value)
# print(eur_pln_timeline)
        
    
plt.plot(eur_pln_timeline, eur_pln_value)
plt.xlabel('data')
plt.ylabel('value')
plt.title('EUR/PLN')
plt.grid()
plt.savefig("eur_pln.png")
plt.show()
        