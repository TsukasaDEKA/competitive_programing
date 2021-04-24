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
        input = """2 2"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 15"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # K <= 2500 なので、X, Y の全探索で間に合いそう。0 <= Z = S - (X+Y) <= K で求まるので。
  K, S = map(int, input().split(" "))

  ans = 0
  for x in range(K+1):
    for y in range(K+1):
      if S - (x+y) >= 0 and S - (x+y) <= K: ans+=1

  print(ans)

resolve()


if __name__ == "__main__":
    unittest.main()
