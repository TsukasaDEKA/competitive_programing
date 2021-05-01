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
FLIP
2
2 0 0
1 1 4"""
        output = """LPFI"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4"""
        output = """ILPF"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = list(input())

  Q = int(input())
  rev = False
  N_2 = 2*N
  for _ in range(Q):
    T, A, B = [int(x)-1 for x in input().split(" ")]
    if T == 0:
      if rev: A, B = (A+N)%N_2, (B+N)%N_2
      S[A], S[B] = S[B], S[A]
    else:
      rev = not rev

  if rev: S = S[N:] + S[:N]
  print("".join(S))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
