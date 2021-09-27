#!/usr/bin/env python
# coding: utf-8

# In[1]:


Roman_Box = {
    
    'I' : 1, 
    'V' : 5, 
    'X' : 10, 
    'L' : 50, 
    'C' : 100, 
    'D' : 500, 
    'M' : 1000,
}

def Roman_to_Dec(RomanNo):
    sum = 0
    for i in range(len(RomanNo) - 1):
        left = RomanNo[i]
        right = RomanNo[i+1]
        
        if Roman_Box[left] < Roman_Box[right]:
            sum -= Roman_Box[left]
        else:
            sum += Roman_Box[left]
    sum += Roman_Box[RomanNo[-1]]
    return sum

