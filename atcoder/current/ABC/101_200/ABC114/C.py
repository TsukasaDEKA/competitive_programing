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
        input = """575"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3600"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """999999999"""
        output = """26484"""
        self.assertIO(input, output)

from collections import deque

def resolve():
  N = int(input())
  # 3, 5, 7 から始まる幅優先探索を行う。3, 5, 7 を使った 10**9 以下の数字は 4**8 == 65536 なので多分間に合う
  # [<元になる数>, 3の出現回数, 5の出現回数, 7の出現回数] をキューに入れて、元になる数が N を超えたら切り上げ
  # 元になる数が N 以下かつ 3, 5, 7 の出現回数が全て 1 以上だったら ans+1
  ans=0

  que_357 = deque()
  que_357.append((3, 1, 0, 0))
  que_357.append((5, 0, 1, 0))
  que_357.append((7, 0, 0, 1))
  while que_357:
    current, three, five, seven = que_357.popleft()
    if current <= N and three >= 1 and five >= 1 and seven >= 1: ans+=1
    if current*10+3 <= N: que_357.append((current*10+3, three+1, five,   seven))
    if current*10+5 <= N: que_357.append((current*10+5, three,   five+1, seven))
    if current*10+7 <= N: que_357.append((current*10+7, three,   five,   seven+1))

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
