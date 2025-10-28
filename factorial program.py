def factorial(a):
  num=1
  for i in range (1,a+1):
    num=num*i
  return num
n=int(input("Enter the number:"))
print(factorial(n))


