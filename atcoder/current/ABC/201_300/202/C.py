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
1 2 2
3 1 2
2 3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 1 1 1
1 1 1 1
1 2 3 4"""
        output = """16"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
2 3 3
1 3 3
1 1 1"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  C = [B[int(x)-1] for x in input().split(" ")]

  aggA = [0]*(N+1)
  aggC = [0]*(N+1)
  for i in range(N):
    aggA[A[i]]+=1
    aggC[C[i]]+=1
  
  ans = 0
  for i in range(1, N+1):
    ans += aggA[i]*aggC[i]

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
