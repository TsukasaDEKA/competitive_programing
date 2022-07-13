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
        input = """3 7
9 3 4"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 6
3 9"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 11
11 3 7 15"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 12
10 2 8 6 4"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  A.sort()
  max_A = A[-1]

  if max_A < K:
    print("IMPOSSIBLE")
    return

  for a in A:
    if a == K or a==1:
      print("POSSIBLE")
      return
  
  base = A[0]
  for a in A[1:]:
    rest = a%base
    if rest == 0: continue
    if K%rest==0:
      print("POSSIBLE")
      return
  print("IMPOSSIBLE")

# resolve()


if __name__ == "__main__":
    unittest.main()
