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
        input = """5
2 6
0 0
1000000 1000000
12345 67890
0 1000000"""
        output = """6
1
0
933184801
500001500001"""
        self.assertIO(input, output)

def resolve():
  T = int(input())
  for _ in range(T):
    # C を固定する。
    ans = 0
    L, R = map(int, input().split(" "))
    diff = R - L
    if diff - L < 0:
      print(ans)
      continue
    length = diff + 1 - L
    print(length*(2+(length-1))//2 )

resolve()

if __name__ == "__main__":
    unittest.main()
