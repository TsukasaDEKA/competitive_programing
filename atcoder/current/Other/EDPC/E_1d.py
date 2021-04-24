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
        input = """3 8
3 3
4 5
5 6"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1000000000
1000000000 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10
  N, W = map(int, input().split(" "))

  items = []
  V = 0
  for _ in range(N):
    item = [int(x) for x in input().split(" ")]
    items.append(item)
    V += item[1]
 
  dp = [inf]*(V+1)
  dp[0] = 0

  max_val_index = 0
  for item in items:
    weight, value = item
    for v in reversed(range(value, V+1)):
      if dp[v-value] + weight <= W:
        dp[v] = min(dp[v-value] + weight, dp[v])
        if dp[v] != inf and v > max_val_index: max_val_index = v
  print(max_val_index)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
