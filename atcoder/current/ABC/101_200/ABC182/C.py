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
        input = """35"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """369"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6227384"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """11"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  N = [int(x) for x in list(input())]
  countN = [0, 0, 0]
  for n in N:
    countN[n%3] += 1

  # print(countN)

  if countN[0] > 0 or countN[1] >= 3 or countN[2] >= 3 or (countN[1] >= 1 and countN[2] >= 1):
    ans = min(abs(countN[1]%3-countN[2]%3), abs(countN[1]-countN[2])%3)
    print(ans)
  else:
    print(-1)
resolve()

if __name__ == "__main__":
    unittest.main()
