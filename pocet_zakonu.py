import csv

soubor= open("sankce.csv", encoding="UTF-8")
csv_reader=csv.reader(soubor, delimiter = ",")

Z1=0
Z2=0
Z3=0
Z4=0
Z5=0
Z6=0
Z7=0
Z8=0
Z9=0
Z10=0
Z11=0
Z12=0
Z13=0
Z14=0
Z15=0
Z16=0
Z17=0
Z18=0
Z19=0
Z20=0
Z21=0
Z22=0
Z23=0
Z24=0
Z25=0
Z26=0
Z27=0
Z28=0
Z29=0
Z30=0
Z31=0
Z32=0
Z33=0
Z34=0
Z35=0
Z36=0

for radek in csv_reader:
  if  "Zák. 634/1992" in radek[3]:
    Z1 += 1
  elif "Zák. 311/2006" in radek[3]:
    Z2 += 1
  elif "Zák. 22/1997" in radek[3]:
    Z3 += 1
  elif "Zák. 102/2001" in radek[3]:
    Z4 += 1
  elif "Zák. 90/2016" in radek[3]:
    Z5 += 1
  elif "Zák. 206/2015" in radek[3]:
    Z6 += 1
  elif "Zák. 477/2001" in radek[3]:
    Z7 += 1
  elif "Zák. 353/2003" in radek[3]:
    Z8 += 1
  elif "Zák. 255/2012" in radek[3]:
    Z9 += 1
  elif "Zák. 65/2017" in radek[3]:
    Z10 += 1
  elif "Zák. 253/2008" in radek[3]:
    Z11 += 1
  elif "Zák. 64/1986" in radek[3]:
    Z12 += 1
  elif "Zák. 259/2014" in radek[3]:  
    Z13 += 1
  elif "Zák. 201/2012" in radek[3]: 
    Z14 += 1  
  elif "Zák. 185/2001" in radek[3]:
    Z15 += 1 
  elif "Zák. 223/2016" in radek[3]:
    Z19 += 1 

  elif "Zák. 145/2010" in radek[3]: 
    Z23 += 1  
  elif "Zák. 552/1991" in radek[3]:
    Z24 += 1 
  elif "Zák. 307/2013" in radek[3]:
    Z25 += 1 
  elif "Zák. 379/2005" in radek[3]:
    Z26 += 1 
  elif "Zák. 379/2005" in radek[3]:
    Z26 += 1 
  elif "Zák. 89/2012" in radek[3]:
    Z27 += 1 
  elif "Zák. 159/1999" in radek[3]:
    Z28 += 1  
  elif "Zák. 257/2016" in radek[3]:
    Z29 += 1  
  elif "Zák. 156/2000" in radek[3]:
    Z30 += 1 
  elif "Zák. 73/2012" in radek[3]:
    Z34 += 1  
  elif "Zák. 247/2006" in radek[3]:
    Z35 += 1    
  elif "Nař. 305/2011" in radek[3]:
    Z16 += 1
  elif "Nař. 1007/2011" in radek[3]:  
    Z17 += 1
  elif "Nař. 2016/425" in radek[3]: 
    Z18 += 1  
  elif "Nař. 524/2013" in radek[3]:
    Z20 += 1
  elif "Nař. 995/2010" in radek[3]:  
    Z21 += 1
  elif "Nař. 2016/426" in radek[3]: 
    Z22 += 1  
  elif "Nař. 2015/751" in radek[3]: 
    Z31 += 1  
  elif "Nař. 2018/302" in radek[3]: 
    Z32 += 1 
  elif "Nař. 1523/2007" in radek[3]: 
    Z33 += 1  
  else:
    Z36+=1

# seznam=[]
# for x in range(Z1, Z36):
#   #seznam.append(x)
#   print(x)

print("Z1: ",Z1, "Z2: ",Z2, "Z3: ",Z3, "Z4: ",Z4, "Z5: ",Z5, "Z6 ",Z6, "Z7: ",Z7, "Z8: ",Z8, "Z9: ",Z9, "Z10: ",Z10, "Z11: ",Z11, "Z12: ",Z12, "Z13: ",Z13, "Z14: ",Z14, "Z15: ",Z15, "Z16: ",Z16,  "Z17: ",Z17, "Z18: ",Z18, "Z20: ",Z20,  "Z21: ",Z21, "Z22: ",Z22, "Z23: ",Z23,  "Z24: ",Z24, "Z25: ",Z25, "Z26: ",Z26,  "Z27: ",Z27, "Z28: ",Z28, "Z29: ", Z29, "Z30: ",Z30, "Z31: ",Z31, "Z32: ", Z32, "Z33: ",Z33, "Z34: ",Z34, "Z35: ", Z35, "Z36: ",Z36)
#print(seznam)
