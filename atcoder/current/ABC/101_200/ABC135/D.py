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
        input = """??2??5"""
        output = """768"""
        self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """?44"""
    #     output = """1"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """7?4"""
    #     output = """0"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???"""
    #     output = """153716888"""
    #     self.assertIO(input, output)

def resolve():
  # 例 3 だと、7?4mod13 = (704 + 10*?)mod13 = 2mod13 + (10*?)mod13
  # なので、(10*?)mod13 = (5-2)mod13 となる ? が何個あるかを探す。
  # この (10*?)mod13 には周期性がある。
  # i*(10**X)mod13 (i = 1 ~ 9) は等差数列になっていて、
  # 差は [1, -3, -4, -1, 3, 4]、初項 [1, 10, 9, 12, 3, 4] である。
  # 順番はあまり意味が無いので、含まれない数に着目してみる。
  # 差が -3, 3 だと 3, 6, 9 が含まれない。
  # 差が -4, 4 だと 4, 8, 12 が含まれない。
  # 差が -1 の場合、1, 2, 3 が含まれない。
  # 差が  1 の場合、10, 11, 12 が含まれない。

  S = list(input())[::-1]
  resource = [ set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 4, 5, 7, 8, 10, 11, 12]), set([1, 2, 3, 5, 6, 7, 9, 10, 11]),
    set([4, 5, 6, 7, 8, 9, 10, 11, 12]), set([1, 2, 3, 5, 6, 8, 9, 11, 12]), set([2, 3, 4, 6, 7, 8, 10, 11, 12])]
  count = [0]*6
  base = 0
  for i in range(len(S)):
    if S[i] == "?": count[i%6]+=1
    else: base+= int(S[i])*(10**i)
  
  target = (5 - base%13)%13

  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
