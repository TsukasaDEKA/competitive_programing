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
        input = """3
1 5 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
10 10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1 3 3 1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 全探索で間に合いそう。
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  temp = A[0]
  for a in A[1:]: temp^=a
  ans = temp

  for i in range(1, 2**(N-1)):
    xor_tar = []
    or_tar = 0
    for j in range(N):
      if i&(1<<j):
        xor_tar.append(or_tar|A[j])
        or_tar = 0
      else:
        or_tar|=A[j]
    temp = or_tar
    for x in xor_tar:
      temp^=x
    ans = min(ans, temp)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
