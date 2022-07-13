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

    def test_Sample_Input_1(self):
        input = """2 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """14 21"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 100"""
        output = """99"""
        self.assertIO(input, output)

def resolve():
  def extgcd(a, b):
    if b:
      g, y, x = extgcd(b, a % b)
      y -= (a // b)*x
      return g, x, y
    return a, 1, 0
  # 互いに素である必要がある。
  # 奇数と偶数 or 奇数と奇数である必要がある。
  # 片方は奇数。
  # extgcd でいける・・？
  inf = 10**18+1
  L, R = map(int, input().split(" "))

  for ans in range(R-L, 0, -1):
    for l in range(L, R-ans+1):
      g, _, _ = extgcd(l, l+ans)
      if g == 1:
        print(ans)
        return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()