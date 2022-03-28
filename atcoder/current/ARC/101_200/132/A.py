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
        input = """5
5 2 3 4 1
4 2 3 1 5
7
1 5
5 1
1 1
2 2
3 3
4 4
5 5"""
        output = """#.#.#.#"""
        self.assertIO(input, output)

def resolve():
  # ただの並べ替え
  inf = 10**18+1
  N = int(input())
  R = [int(x)-1 for x in input().split(" ")]
  C = [int(x)-1 for x in input().split(" ")]

  Q = int(input())
  ans = []
  for _ in range(Q):
    r, c = [int(x)-1 for x in input().split(" ")]
    r = R[r]
    c = C[c]
    # print(r, c, "#" if N-1-r <= c else ".")
    ans.append("#" if N-1-r <= c else ".")
  print("".join(ans))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()