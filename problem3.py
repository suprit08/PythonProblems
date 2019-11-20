#diffprob.py

#User input
n = int(input("Enter any number : "))

#sum of squares of first 'n'
i,j,x,c=0,0,0,0
for i in range(1,n+1):
    j = i*i
    x =  x+j
print("Sum of squares of first %d natural numbers : %d"%(n,x))

#squares of the sum of the first 'n'
for i in range(1,n+1):
    j = i
    c = c + j
print("Squares of sum of first %d natural numbers : %d"%(n,(c*c)))

#Difference calculation
cal = (c*c)-x
print("Difference = ",cal)