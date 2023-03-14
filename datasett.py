import csv
import matplotlib.pyplot as plt
import numpy as np
filnavn = "KlimaProsjekt/klima.csv"

aarstall = []
metan = []
karbondioksid = []
klimagasser = []
s = slice(0, 32)

with open(filnavn, encoding="iso-8859-1") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    overskrifter = next(filinnhold)
    #print(overskrifter)
    
    for rad in filinnhold:
        if rad[5] == '.':
            continue
        if rad[2] == 'A10 Klimagasser i alt':
            klimagasser.append(int(rad[5]))
            aarstall.append(int(rad[3]))
        elif rad[2] == 'K11 Karbondioksid (CO2)':
            karbondioksid.append(int(rad[5]))
        elif rad[2] == 'K12 Metan (CH4)':
            metan.append(int(rad[5]))
            

#print(klimagasser[s])
#print(karbondioksid[s])
#print(aarstall[s])
#print(metan[s])
            
plt.plot(aarstall[s], klimagasser[s], aarstall[s], karbondioksid[s], aarstall[s], metan[s])
plt.xlabel("Årstall")
plt.ylabel("1000 tonn")
plt.gca().legend(('Klimagasser', 'Karbondioksid', "Metan"))
plt.show()
