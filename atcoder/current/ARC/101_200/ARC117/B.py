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
        input = """2
1 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
1 2 3 4 5 5"""
        output = """32"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
159 265 314 323 358 846 979"""
        output = """492018656"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  N = int(input())
  A = [0] + sorted([int(x) for x in input().split(" ")])
  ans = 1
  for i in range(N):
    ans *= A[i+1] - A[i] + 1
    if ans >= mod: ans%=mod
  print(ans)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
