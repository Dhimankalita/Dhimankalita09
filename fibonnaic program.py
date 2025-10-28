n=int(input("enter a no"))
num1=0
num2=1
print(num1,end=" ")
print(num2,end=" ")
for i in range(1,n+1):
     x=num1+num2
     num1=num2
     num2=x
     print(x,end=" ")

