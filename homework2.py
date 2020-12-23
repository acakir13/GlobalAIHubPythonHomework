#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input('Please share your name :')
surname = input ('Please share your surname:')
age = int(input('Please share your age:'))
year = int(input('Please enter your birth year:'))

data = [name, surname, age, year]

for i in data:
    
    print(i)
    
if age < 18:
    print("You can not go out because it is so dangerous.")
elif age>= 18:
    print("You can go to street.")    
else:
  print("Invalid Enter")


# In[ ]:




