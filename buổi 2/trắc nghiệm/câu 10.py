import math

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def approx_sin(x, n):
  result = 0
  for i in range(1, n+1):
    result += (-1)**(i-1) * x**(2*i-1) / factorial(2*i-1)
  return result
assert round ( approx_sin ( x =1 , n =10) , 4) ==0.8415
print ( round ( approx_sin ( x =3.14 , n =10) , 4) )