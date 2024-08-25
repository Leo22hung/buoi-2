import numpy as np

def md_nre(y_true, y_pred, n, p):
  """Tính toán Mean Difference of nth Root Error (MD_nRE)"""
  diff = np.abs(np.power(y_true, 1/n) - np.power(y_pred, 1/n))
  return np.mean(np.power(diff, p))

# Ví dụ sử dụng
y_true = np.array([100, 50, 20, 5.5, 1.0, 0.0])
y_pred = np.array([99.5, 49.5, 19.5, 5.0, 0.5, 0.1])
n = 2
p = 1

md_nre_result = md_nre(y_true, y_pred, n, p)
print("MD_nRE:", md_nre_result)