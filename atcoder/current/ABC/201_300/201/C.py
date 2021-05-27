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
        input = """ooo???xxxx"""
        output = """108"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """o?oo?oxoxo"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """xxxxx?xxxo"""
        output = """15"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter
  inf = 10**18+1
  S = list(input())
  needed = set()
  for i in range(10):
    if S[i] == "o":
       needed.add(i)
  count_S = Counter(S)
  if count_S["o"] > 4 or count_S["x"] == 10:
    print(0)
    return

  # print(S)
  ans = 0
  for i_0 in range(10):
    for i_1 in range(10):
      for i_2 in range(10):
        for i_3 in range(10):
          if S[i_0] == "x" or S[i_1] == "x" or S[i_2] == "x" or S[i_3] == "x": continue
          count = set()
          count.add(i_0)
          count.add(i_1)
          count.add(i_2)
          count.add(i_3)
          if count_S["o"] > len(count): continue
          for n in needed:
            if n not in count: break
          else:
            ans += 1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
