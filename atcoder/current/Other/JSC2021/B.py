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
        input = """2 2
1 2
1 3"""
        output = """2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
1 2 3 4
1 2 3 4"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  ans = defaultdict(int)
  for a in A:
    ans[a]+=1
  for b in B:
    ans[b]+=1
  ans = [key for key, val in ans.items() if val == 1]
  ans.sort()


  print(*ans, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
