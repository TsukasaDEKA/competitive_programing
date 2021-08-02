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
        input = """9"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """119"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10000000"""
        output = """24"""
        self.assertIO(input, output)


def resolve():
  # 大きい方から貪欲？
  P = int(input())
  money = []
  money.append(0)
  money.append(1)
  for i in range(2, 10**7+1):
    money.append(money[-1]*i)
    if money[-1] >= P: break

  count = 0
  for i in reversed(range(1, len(money))):
    while P>=money[i]:
      P-=money[i]
      count += 1
    if P == 0: break
  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()