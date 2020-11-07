# -*- coding: utf-8 -*-
"""


@author: saurav
"""

cityname = []
for i in range(0,5):
    city=input('Enter 5 Elements: ')
    cityname.append(city)
print(cityname)  
srch = input('Eneter element to find:  ')
for i in range(0,5):
    if (srch == cityname[i]):
        print("Found element at position:",i+1)
        break
    elif (srch != cityname[i]):
        print('Not Found')
        break
        
    
    
