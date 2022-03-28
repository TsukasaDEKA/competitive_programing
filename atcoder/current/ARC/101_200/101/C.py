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
        input = """5 3
-30 -10 10 20 50"""
        output = """40"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
10 20 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1
0"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8 5
-9 -7 -4 -3 1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  inf = K*10**8+1
  X = [int(x) for x in input().split(" ")]


  ans = inf
  for i in range(N-K+1):
    left, right = X[i], X[i+K-1]
    cost = 0
    if left <= 0 and right <= 0:
      cost = abs(left)
    elif left >= 0 and right >= 0:
      cost = abs(right)
    else:
      cost = 2*min(abs(left), abs(right)) + max(abs(left), abs(right))
    ans = min(ans, cost)
  print(ans)
  # print(ans if ans!=inf else 0)

# resolve()

if __name__ == "__main__":
    unittest.main()
