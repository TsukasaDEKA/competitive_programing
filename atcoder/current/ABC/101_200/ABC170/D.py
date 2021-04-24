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
24 11 8 3 16"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
5 5 5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
33 18 45 28 8 19 89 86 2 4"""
        output = """5"""
        self.assertIO(input, output)


#     def test_Sample_Input_3(self):
#         input = """10
# 2 3 4 5 6 7 8 9 10"""
#         output = """1"""
#         self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  A.sort()
  # setA = set(A)
  maxA = max(A)
  DP = [True] * (maxA + 1)
  answers = []

  for a in A:
    if not DP[a]:
      if len(answers):
        if answers[-1] == a:
          del answers[-1]
      continue
    answers.append(a)

    for i in range(a, maxA+1, a): DP[i] = False
  print(len(answers))

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
