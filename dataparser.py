#! /usr/bin/env python
#Use as: python dataparser.py [filename]

import sys
import numpy as np
import matplotlib.pyplot as plt
#limits are 10^x
AUmin=-2
AUmax=2
Massmin=0
Massmax=4

filename=sys.argv[1]
data=np.loadtxt(filename, dtype='str')

coremass=data[:,2].astype(float)
envelopemass=data[:,3].astype(float)
ratio=envelopemass/coremass
totalmass=coremass+envelopemass
semimajoraxis=data[:,9].astype(float)
iceline=data[:,22].astype(float)
formdist=data[:,23].astype(float)

#gas is envelope > 10x core
#ice is formed outside iceline
#rocky formed inside iceline
gas=[]
rocky=[]
icy=[]

for i in range(len(data)):
   if ratio[i]>10: gas.append(i)
   else:
      if iceline[i]<formdist[i]: icy.append(i)
      else: rocky.append(i)


print np.where(ratio > 10)[0]

plt.figure(1)
plt.scatter(semimajoraxis, totalmass)
plt.yscale('log')
plt.ylim([pow(10,Massmin),pow(10,Massmax)])
plt.xlim([pow(10,AUmin),pow(10,AUmax)])
plt.xscale('log')
plt.xlabel('Semi-major axis (AU)')
plt.ylabel('Total Mass (M_e)')
plt.figure(2)
plt.scatter(semimajoraxis[gas], totalmass[gas], color='red', label='Gas')
plt.scatter(semimajoraxis[rocky], totalmass[rocky], color='green', label='Rocky')
plt.scatter(semimajoraxis[icy], totalmass[icy], color='blue', label='Icy')
plt.yscale('log')
plt.ylim([pow(10,Massmin),pow(10,Massmax)])
plt.xlim([pow(10,AUmin),pow(10,AUmax)])
plt.xscale('log')
plt.xlabel('Semi-major axis (AU)')
plt.ylabel('Total Mass (M_e)')
plt.legend()
plt.figure(3)
bins=np.logspace(-2, 2, num=50)
plt.hist([semimajoraxis[gas],semimajoraxis[rocky],semimajoraxis[icy]], bins=bins, stacked=True, color=['red', 'green', 'blue'], label=['Gas', 'Rocky', 'Icy'])
plt.legend()
plt.xscale('log')
plt.xlabel('Semi-major axis (AU)')
plt.xlim([pow(10,AUmin),pow(10,AUmax)])
plt.ylabel('Count')
plt.figure(4)
bins=np.logspace(0, 4, num=50)
plt.hist([totalmass[gas],totalmass[rocky],totalmass[icy]], bins=bins, stacked=True, color=['red', 'green', 'blue'], label=['Gas', 'Rocky', 'Icy'])
plt.legend()
plt.xscale('log')
plt.xlabel('Total Mass (M_e)')
plt.xlim([pow(10,Massmin),pow(10,Massmax)])
plt.ylabel('Count')
plt.show()
print "Gas planets:", len(gas)
print "Rocky planets:", len(rocky)
print "Icy planets:", len(icy)
print "Total planets:", len(gas)+len(rocky)+len(icy)
