import math

def calc_sigmoid(x):
  return 1 / (1 + math.exp(-x))

def calc_relu(x):
  return max(0, x)

def calc_elu(x, alpha=0.01):
  return alpha * (math.exp(x) - 1) if x <= 0 else x

def calc_activation_func(x, act_name):
  if act_name == 'sigmoid':
    return calc_sigmoid(x)
  elif act_name == 'relu':
    return calc_relu(x)
  elif act_name == 'elu':
    return calc_elu(x)
  else:
    raise ValueError("Invalid activation function")

# Kiểm tra kết quả
assert calc_activation_func(x=1, act_name='relu') == 1
print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))