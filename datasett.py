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

utslipp_1990 = []
utslipp_1991 = []
utslipp_1992 = []
utslipp_1993 = []
utslipp_1994 = []
utslipp_1995 = []
utslipp_1996 = []
utslipp_1997 = []
utslipp_1998 = []
utslipp_1999 = []
utslipp_2000 = []
utslipp_2001 = []
utslipp_2002 = []
utslipp_2003 = []
utslipp_2004 = []
utslipp_2005 = []
utslipp_2006 = []
utslipp_2007 = []
utslipp_2008 = []
utslipp_2009 = []
utslipp_2010 = []
utslipp_2011 = []
utslipp_2012 = []
utslipp_2013 = []
utslipp_2014 = []
utslipp_2015 = []
utslipp_2016 = []
utslipp_2017 = []
utslipp_2018 = []
utslipp_2019 = []
utslipp_2020 = []
utslipp_2021 = []
#slice for å skrive ut verdiene fra 1990-2021
s = slice(0, 32)

#åpner csv filen slik at python kan hente ut dataen man ønsker
with open(filnavn, encoding="iso-8859-1") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)
    print(overskrifter)
    
    #her lages en loop som leser gjennom hele csv filen
    for rad in filinnhold:
        if rad[5] == '.' or rad[5] == '-': #Hvis loopen finner noe som ikke er tallverdi vil det bli ignorert.
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
            
        if rad[3] == '1990':
            utslipp_1990.append(int(rad[5]))
        elif rad[3] == '1991':
            utslipp_1991.append(int(rad[5]))
        elif rad[3] == '1992':
            utslipp_1992.append(int(rad[5]))
        elif rad[3] == '1993':
            utslipp_1993.append(int(rad[5]))
        elif rad[3] == '1994':
            utslipp_1994.append(int(rad[5]))
        elif rad[3] == '1995':
            utslipp_1995.append(int(rad[5]))
        elif rad[3] == '1996':
            utslipp_1996.append(int(rad[5]))
        elif rad[3] == '1997':
            utslipp_1997.append(int(rad[5]))
        elif rad[3] == '1998':
            utslipp_1998.append(int(rad[5]))
        elif rad[3] == '1999':
            utslipp_1999.append(int(rad[5]))
        elif rad[3] == '2000':
            utslipp_2000.append(int(rad[5]))
        elif rad[3] == '2001':
            utslipp_2001.append(int(rad[5]))
        elif rad[3] == '2002':
            utslipp_2002.append(int(rad[5]))
        elif rad[3] == '2003':
            utslipp_2003.append(int(rad[5]))
        elif rad[3] == '2004':
            utslipp_2004.append(int(rad[5]))
        elif rad[3] == '2005':
            utslipp_2005.append(int(rad[5]))
        elif rad[3] == '2006':
            utslipp_2006.append(int(rad[5]))
        elif rad[3] == '2007':
            utslipp_2007.append(int(rad[5]))
        elif rad[3] == '2008':
            utslipp_2008.append(int(rad[5]))
        elif rad[3] == '2009':
            utslipp_2009.append(int(rad[5]))
        elif rad[3] == '2010':
            utslipp_2010.append(int(rad[5]))
        elif rad[3] == '2011':
            utslipp_2011.append(int(rad[5]))
        elif rad[3] == '2012':
            utslipp_2012.append(int(rad[5]))
        elif rad[3] == '2013':
            utslipp_2013.append(int(rad[5]))
        elif rad[3] == '2014':
            utslipp_2014.append(int(rad[5]))
        elif rad[3] == '2015':
            utslipp_2015.append(int(rad[5]))
        elif rad[3] == '2016':
            utslipp_2016.append(int(rad[5]))
        elif rad[3] == '2017':
            utslipp_2017.append(int(rad[5]))
        elif rad[3] == '2018':
            utslipp_2018.append(int(rad[5]))
        elif rad[3] == '2019':
            utslipp_2019.append(int(rad[5]))
        elif rad[3] == '2020':
            utslipp_2020.append(int(rad[5]))
        elif rad[3] == '2021':
            utslipp_2021.append(int(rad[5]))
        
                
            
            
#print(utslipp_1990)
#print(utslipp_1991)
#print(utslipp_1992)

#printer ut og tar med "s" variablen som gjør at listen ikke printer ut alle verdiene i csv filen
#print("år: ", aarstall[s])
#print("Klimagasser: ", klimagasser[s])
#print("Karbondioksid: ", karbondioksid[s])
#print("Metan: ", metan[s])
#bruker "s" variablen for å gjøre grafen riktig her også   
