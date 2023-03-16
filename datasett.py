import csv
import matplotlib.pyplot as plt
import numpy as np
filnavn = "KlimaProsjekt/klima.csv"

aarstall = []
metan = []
karbondioksid = []
klimagasser = []

lystgass = []
hydrofluorkarboner = []
perflurokarboner = []
svovelheksafluorid = []

#slice for å skrive ut verdiene fra 1990-2021
s = slice(0, 32)

#åpner csv filen slik at python kan hente ut dataen man ønsker
with open(filnavn, encoding="iso-8859-1") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    print(overskrifter)
    
    #her lages en loop som leser gjennom HELE csv filen
    for rad in filinnhold:
        if rad[5] == '.' or rad[5] == '-': #Siden det er punktum i csv fil for verdiene skal loopen ignorere hver gang det kommer punktum.
            continue
        #looper radene og legger til verdiene med "int" parameter for klimagasser, karbondioksid og metan i egne lister
        if rad[2] == 'A10 Klimagasser i alt':
            klimagasser.append(int(rad[5]))
            aarstall.append(int(rad[3]))
        elif rad[2] == 'K11 Karbondioksid (CO2)':
            karbondioksid.append(int(rad[5]))
        elif rad[2] == 'K12 Metan (CH4)':
            metan.append(int(rad[5]))
        elif rad[2] == 'K13 Lystgass (N2O)':
            lystgass.append(int(rad[5]))
        elif rad[2] == 'K80 Hydrofluorkarboner (HFK)':
            hydrofluorkarboner.append(int(rad[5]))
        elif rad[2] == 'K90 Perfluorkarboner (PFK)':
            perflurokarboner.append(int(rad[5]))
        elif rad[2] == 'K95 Svovelheksafluorid (SF6)':
            svovelheksafluorid.append(int(rad[5]))
            
            
            
            
            
            
#printer ut og tar med "s" variablen som gjør at listen ikke printer ut alle verdiene i csv filen
print("år: ", aarstall[s])
print("Klimagasser: ", klimagasser[s])
print("Karbondioksid: ", karbondioksid[s])
print("Metan: ", metan[s])


#bruker "s" variablen for å gjøre grafen riktig her også   
plt.plot(aarstall[s], klimagasser[s], aarstall[s], karbondioksid[s], aarstall[s], metan[s])
plt.xlabel("Årstall")
plt.ylabel("1000 tonn")
plt.grid()
plt.gca().legend(('Klimagasser', 'Karbondioksid', "Metan"))
plt.show()

plt.plot(aarstall[s], lystgass[s], aarstall[s], hydrofluorkarboner[s], aarstall
         [s], perflurokarboner[s], aarstall[s], svovelheksafluorid[s])

plt.xlabel("Årstall")
plt.ylabel("1000 tonn")
plt.grid()
plt.gca().legend(('Lystgass', 'Hydrofluorkarboner', "Perfluorkarboner", "Svovelheksafluorid"))
plt.show()
