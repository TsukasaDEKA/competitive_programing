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
        input = """15"""
        output = """23"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """13"""
        output = """21"""
        self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """100000"""
    #     output = """3234566667"""
    #     self.assertIO(input, output)

from collections import deque

def resolve():
  K = int(input())
  lunlun_list = [0]*(K+1)
  lunlun_index = 0
  # 1 ~ 10**5 までのルンルン数を求める。
  # N=10**2
  # 幅優先探索して桁を足していく感じにする。

  next_lunluns = deque(list(range(1, 10)))
  while lunlun_index <= K:
    lunlun = next_lunluns.popleft()
    lunlun_list[lunlun_index] = lunlun
    lunlun_index+=1

    if lunlun_index == K:
      print(lunlun)
      return

    first_digit = lunlun%10
    for n in range(max(0, first_digit-1), min(10, first_digit+2)):
      next_lunluns.append(lunlun*10 + n)
resolve()

if __name__ == "__main__":
    unittest.main()
