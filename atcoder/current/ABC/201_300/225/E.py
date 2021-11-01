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
        input = """3
1 1
2 1
1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
414598724 87552841
252911401 309688555
623249116 421714323
605059493 227199170
410455266 373748111
861647548 916369023
527772558 682124751
356101507 249887028
292258775 110762985
850583108 796044319"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  from decimal import Decimal
  from fractions import Fraction

  inf = 10**20+1
  N = int(input())
  DEG = []
  for _ in range(N):
    x, y = input().split(" ")
    x = Decimal(x)
    y = Decimal(y)
    y_1 = y-Decimal("1")
    x_1 = x-Decimal("1")
    min_ = y_1/x
    max_ = y/x_1 if x_1 != 0 else inf
    DEG.append((min_, max_))
  
  DEG.sort(key=lambda x: x[1])
  # print(DEG)
  ans = 0
  current = 0
  for i in range(N):
    x, y = DEG[i]
    if x >= current:
      ans+=1
      current = y

  print(ans)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()