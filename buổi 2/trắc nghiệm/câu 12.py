import math

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def approx_cosh(x, n):
  result = 0
  for i in range(n+1):
    result += x**(2*i) / factorial(2*i)
  return result
assert round ( approx_cosh ( x =1 , n =10) , 2) ==1.54
print ( round ( approx_cosh ( x =3.14 , n =10) , 2) )
# Đáp án : A