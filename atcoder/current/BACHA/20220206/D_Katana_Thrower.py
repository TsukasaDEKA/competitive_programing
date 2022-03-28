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
        input = """1 10
3 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 10
3 5
2 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 1000000000
1 1
1 10000000
1 30000000
1 99999999"""
        output = """860000004"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 500
35 44
28 83
46 62
31 79
40 43"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  # a_i が最強の剣を振りまくった上で a_i < b_j となる全ての剣を投げつけた時に HP <= 0 となる回数を考える。
  inf = 10**18+1
  N, H = map(int, input().split(" "))
  A_B = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])
  max_A = A_B[-1][0]
  A_B.sort(key=lambda x: x[1], reverse=True)

  ans = 0
  for _, b in A_B:
    if b <= max_A: break
    ans+=1
    H-=b
    if H<=0:
      H=0
      break
  ans += (H+max_A-1)//max_A
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()