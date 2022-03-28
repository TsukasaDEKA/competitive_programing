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
        input = """2 40
3 1 8 4
2 10 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 200
3 10 10 10
3 10 10 10
5 2 2 2 2 2"""
        output = """45"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 1000000000000000000
2 1000000000 1000000000
2 1000000000 1000000000
2 1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter, defaultdict

  N, X = map(int, input().split(" "))
  A = []
  for i in range(N):
    a = [int(x) for x in input().split(" ")]
    A.append(Counter(a[1:]))

  ans = defaultdict(int)
  for key, val in A[0].items():
    ans[key]+=val

  for i in range(1, N):
    temp = defaultdict(int)
    for key, val in A[i].items():
      if key > X: continue
      for current_key, current_val in ans.items():
        if current_key * key > X: continue
        temp[current_key * key]+=val*current_val
    ans = temp
  print(ans[X])


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()