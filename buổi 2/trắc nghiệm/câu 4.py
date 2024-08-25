import math

def calc_sig(x):
  return 1 / (1 + math.exp(-x))

# Kiểm tra kết quả
assert round(calc_sig(3), 2) == 0.95
print(round(calc_sig(2), 2))
# Đáp án : A