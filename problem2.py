#Pallindromic Triangle

i,j,k=0,0,0

#user input
n = int(input("Enter the n number: "))

#Iterating
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print("")

