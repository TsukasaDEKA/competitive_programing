# 拡張ユークリッドの互除法
def extgcd(a, b):
  if b:
    g, y, x = extgcd(b, a % b)
    y -= (a // b)*x
    return g, x, y
  return a, 1, 0

mod = 7
sample = (mod, 3)
print(extgcd(*sample))