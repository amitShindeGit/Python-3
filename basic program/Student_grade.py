# -*- coding: utf-8 -*-
"""


@author: saurav
"""

print("Please enter your marks for 5 subjects: ")
i=0
sum=0
while i<5:
    num=int(input())
    sum=sum+num
    i+=1
sum=(sum/500)*100
print()
print("Percentage =",sum)
if sum>=85:
    print("Grade is A:")
elif sum>=75:
    print("Grade is B:")
elif sum>=65:
    print("Grade is C:")
elif sum>=55:
    print("Grade is D:")
elif sum>=45:
    print("Grade is E:")
else:
    print("Grade is F:")