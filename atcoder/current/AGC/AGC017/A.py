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
        input = """2 0
1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
50"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 0
1 1 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """45 1
17 55 85 55 74 20 90 67 40 70 39 89 91 50 16 24 14 43 24 66 25 9 89 71 41 16 53 13 61 15 85 72 62 67 42 26 36 66 4 87 59 91 4 25 26"""
        output = """17592186044416"""
        self.assertIO(input, output)

def resolve():
  # 奇数、偶数で分けると良さそう。
  N, P = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  even = 0
  odd = 0
  for a in A:
    if a%2: odd+=1
    else: even+=1

  if odd == 0 and P == 1:
    print(0)
    return

  # 偶数の選び方
  even_pattern = 2**even
  # 奇数を奇数個選ぶのと奇数を偶数個選ぶパターンはそれぞれ同じだけあるので、(2**odd)//2
  odd_pattern = 2**(max(odd-1, 0))

  print(even_pattern * odd_pattern)

resolve()

if __name__ == "__main__":
    unittest.main()
