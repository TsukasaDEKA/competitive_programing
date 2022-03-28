import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
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
2 4 3"""
        output = """63"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
10"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
853983 14095 543053 143209 4324 524361 45154"""
        output = """206521341"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
1 2 3 4 5"""
        output = """243"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  # 全ての部分列なのでソートしても大丈夫
  # 計算量落としきれない。
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])

  for d in range(3, N):
    power = pow(2, d-1)-2
    for i in range(N-d):
      diff += power*(A[i]*A[i+d])
    if diff >= mod: diff%=mod
  print((sum_A**2 + diff)%mod)

# resolve()

if __name__ == "__main__":
    unittest.main()
