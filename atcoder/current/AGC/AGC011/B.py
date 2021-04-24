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
3 1 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 1 1 1 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
40 1 30 2 7 20"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  # 小さい順に並べて順に大きさを足していく。途中で吸収できなくなったら count を リセットする。
  A.sort()

  current_size = A[0]
  count = 1
  for a in A[1:]:
    if a <= 2*current_size:
      count+=1
    else:
      count=1
    current_size+=a

  print(count)

resolve()

if __name__ == "__main__":
    unittest.main()
