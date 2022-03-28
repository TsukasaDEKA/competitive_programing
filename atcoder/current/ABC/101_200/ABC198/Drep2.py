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
        input = """a
b
c"""
        output = """1
2
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """x
x
y"""
        output = """1
1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """p
q
p"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """abcd
efgh
ijkl"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """send
more
money"""
        output = """9567
1085
10652"""
        self.assertIO(input, output)

def resolve():
  from itertools import permutations
  from collections import defaultdict

  inf = 10**18+1
  S = [list(input()) for _ in range(3)]
  target = set()
  for i in range(3):
    for s in S[i]: target.add(s)
    
  if len(target) > 10:
    print("UNSOLVABLE")
    return

  N = len(target)
  target = list(target)
  range_s = [str(x) for x in range(10)]
  for p in permutations(range_s, N):
    def_dict = defaultdict(int)
    for i in range(N):
      def_dict[target[i]] = p[i]
    
    for i in range(3):
      if def_dict[S[i][0]] == "0":
        break
    else:
      s0 = int("".join([def_dict[x] for x in S[0]]))
      s1 = int("".join([def_dict[x] for x in S[1]]))
      s2 = int("".join([def_dict[x] for x in S[2]]))
      if s0 + s1 == s2:
        print(s0, s1, s2, sep="\n")
        return
  print("UNSOLVABLE")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()