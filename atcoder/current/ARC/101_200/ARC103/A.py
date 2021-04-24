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
        input = """4
3 1 3 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
105 119 105 119 105 119"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1 1 1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2
1 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """2
1 1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 偶数番と奇数番でほぼ独立に考えられる
  # 2種類の数が必要な点に注意
  from collections import Counter

  N = int(input())
  V = [int(x) for x in input().split(" ")]

  count_V1 = sorted(Counter(V[::2]).items(), key=lambda x: x[1], reverse=True)
  count_V2 = sorted(Counter(V[1::2]).items(), key=lambda x: x[1], reverse=True)

  if count_V1[0][0] != count_V2[0][0]:
    ans = N - count_V1[0][1] - count_V2[0][1]
  elif len(count_V1)==1 and len(count_V2)==1:
    ans = N - count_V1[0][1]
  elif len(count_V1)==1:
    ans = N - count_V1[0][1] - count_V2[1][1]
  elif len(count_V2)==1:
    ans = N - count_V1[1][1] - count_V2[0][1]
  else:
    ans = N - max(count_V1[1][1] + count_V2[0][1], count_V1[0][1] + count_V2[1][1])
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
