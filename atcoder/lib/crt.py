def extgcd(a, b):
  # ax + by = d (d = 最大公約数) とした時、d, x, y を返す。
  if b:
    g, y, x = extgcd(b, a % b)
    y -= (a // b)*x
    return g, x, y
  return a, 1, 0

# 参考: https://qiita.com/drken/items/ae02240cd1f8edfc86fd
def crt(b1, m1, b2, m2, d=None, p=None, q=None):
  # x ≡ b1 (mod m1)、x ≡ b2 (mod m2) <=> x ≡ r (mod lcm(m1, m2)) となる x, r を返す。
  # また、解が存在しない時、それを示す。
  if d is None: d, p, q = extgcd(m1, m2)
  # 解が存在しない場合 => m1, m2 が互いに素ではなく、かつ b1 ≡ b2 (mod. gcd(m1, m2)) が成立しない。
  if d != 1 and b1%d != b2%d: return -1, -1
  x = b1 + m1*p*(b2-b1)//d
  r = x%((m1*m2)//d)
  return x, r

sample = [2, 7, 4, 13]
print(crt(*sample)) # (30, 30)
