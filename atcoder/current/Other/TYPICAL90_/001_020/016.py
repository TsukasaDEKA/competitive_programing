import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

#     def test_入力例_1(self):
#         input = """227
# 21 47 56"""
#         output = """5"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """9999
# 1 5 10"""
#         output = """1004"""
#         self.assertIO(input, output)

    def test_入力例_3(self):
        input = """998244353
314159 265358 97932"""
        output = """3333"""
        self.assertIO(input, output)

#     def test_入力例_4(self):
#         input = """100000000
# 10001 10002 10003"""
#         output = """9998"""
#         self.assertIO(input, output)


def resolve():
  def extgcd(a, b):
    if b:
      g, y, x = extgcd(b, a % b)
      y -= (a // b)*x
      return g, x, y
    return a, 1, 0

  inf = 9999
  # 合計 9999 枚以下で支払うことができるので全探索が楽に実装できそう。
  N = int(input())
  A, B, C = sorted([int(x) for x in input().split(" ")], reverse=True)

  ans = inf
  g, x, y = extgcd(B, C)
  print(x, y)
  for a in reversed(range(N//A+1)):
    tempA = A*a
    if (N - tempA)%g: continue
    for b in range((N - tempA)//B+1):
      ans = min(ans, a+b+(N - tempA - B*b)//C)
  print(ans)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
