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
9 6 14 1 8
2 10 3 12 11
15 13 5 7 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
10
20
30"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1 1 1
1 1 2
2 2 2"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # サンプルが齢・・・
  # ソートしたらOK?
  # ずらすとより良い結果になるかも => ならないっぽい
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  B = sorted([int(x) for x in input().split(" ")])
  C = sorted([int(x) for x in input().split(" ")])

  ans = 0
  b = c = 0
  for a in range(N):
    while B[b] <= A[a]:
      b+=1
      if b >= N:
        print(ans)
        return
    while C[c] <= B[b]:
      c+=1
      if c >= N:
        print(ans)
        return
    # print(A[a], B[b], C[c])
    ans += 1
    b+=1
    c+=1
    if b >= N or c>=N:
      print(ans)
      return
     
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()