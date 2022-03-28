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
        input = """7
1110110
1010111"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_1(self):
        input = """6
001101
110010"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20
11111000000000011111
11111000000000011111"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
111100
111000"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """119
10101111011101001011111000111111101011110011010111111111111111010111111111111110111111110111110111101111111111110111011
11111111111111111111111111011111101011111011110111110010100101001110111011110111111111110010011111101111111101110111011"""
        output = """22"""
        self.assertIO(input, output)

def resolve():
  # O(N) でいけそう。
  # 1 を持ってこなきゃいけない状況にはならない？ => そんなことはない。
  # 右側にある最寄りの 0 と最寄りの 1 を記録していく？
  # 最寄りの 0 と最寄りの 1 は一度しか使えないので、キューに入れておくか。
  # ダメっぽい。
  # 0 をどこに送るか考える。
  # 0 同士の同線は重なることはない。
  # 0 のインデックス同士を比較していけばいい。
  from collections import deque
  N = int(input())
  S = list(input())
  T = list(input())
  S_zero = []
  T_zero = []
  for i in range(N):
    if S[i] == "0": S_zero.append(i)
    if T[i] == "0": T_zero.append(i)

  if len(S_zero) != len(T_zero):
    print(-1)
    return

  ans = 0 
  for s, t in zip(S_zero, T_zero):
    if s != t: ans+=1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
