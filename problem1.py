#EmailValid.py
from re import *

i,j=0,0

email_list = []
derived_list = []

#input Section
n = int(input("Enter the no. of inputs : "))
while(i<n):
    email_list.append(input("Enter the email address:"))
    i = i + 1

# Deriving Email from inputs
print("-"*50)
print("Valid Output:")

for j in range(0,n):
    match = finditer("\S+@\S+.com",email_list[j])

    for mail in match:
        print(mail.group())
        
            
    