import math

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def approx_sinh(x, n):
  result = 0
  for i in range(1, n+1):
    result += x**(2*i-1) / factorial(2*i-1)
  return result
assert round ( approx_sinh ( x =1 , n =10) , 2) ==1.18
print ( round ( approx_sinh ( x =3.14 , n =10) , 2) )