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
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = input()
  head = ""
  tail = ""
  Q = int(input())
  rev = False
  for _ in range(Q):
    q = input().split(" ")
    if q[0] == "1": rev= not rev
    else:
      f, c = q[1:]
      if (f == "1") ^ rev:
        head += c
      else:
        tail += c
  if not rev:
    print(head[::-1], S, tail, sep="")
  else:
    print(tail[::-1], S[::-1], head, sep="")

resolve()

if __name__ == "__main__":
    unittest.main()
