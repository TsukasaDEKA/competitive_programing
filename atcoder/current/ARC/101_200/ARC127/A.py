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
        input = """11"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """120"""
        output = """44"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """987654321"""
        output = """123456789"""
        self.assertIO(input, output)

def resolve():
  # 1 を連続で並べる。
  # 残りの数値が何パターン作れるか計算する。
  # 場合分けクソめんどくさそう。

  N = int(input())
  lenN = len(str(N))
  ans = 0
  for a in range(1, lenN+1):
    # 1 が先頭に a 個並んでいる数字
    base = 0
    for i in range(a):
      base+=pow(10, i)

    # パターン数を計算する。
    pattarn = 0
    for i in range(lenN+1-a):
      temp = 0
      if N//pow(10, i) < base: break
      if N//pow(10, i) == base:
        # ここの処理が複雑
        if i == 0:
          temp += 1
        else:
          # 一旦下半分に区切る。
          lower = N%pow(10, i)
          for top in range(10):
            if top == 1 or top > lower//pow(10, i-1): continue
            if top < lower//pow(10, i-1):
              temp += pow(10, i-1)
            elif top == lower//pow(10, i-1):
              temp += lower%pow(10, i-1)+1
      if N//pow(10, i) > base:
        if i: temp += 9*pow(10, i-1)
        else: temp += 1
      pattarn+=temp
    # print(a, pattarn, base)
    ans += a*pattarn
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()