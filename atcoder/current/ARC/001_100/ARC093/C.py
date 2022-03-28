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
3 5 -1"""
        output = """12
8
10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 1 1 2 0"""
        output = """4
4
4
2
4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
-679 -2409 -3258 3095 -3291 -4462"""
        output = """21630
21630
19932
8924
21630
19288"""
        self.assertIO(input, output)

def resolve():
  N = int(input())+2
  A = [0]+[int(x) for x in input().split(" ")]+[0]
  base_cost = 0
  for i in range(1, N):
    base_cost += abs(A[i]-A[i-1])

  for i in range(1, N-1):
    ans = base_cost
    ans-=abs(A[i]-A[i-1])
    ans-=abs(A[i]-A[i+1])
    ans+=abs(A[i-1]-A[i+1])
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()