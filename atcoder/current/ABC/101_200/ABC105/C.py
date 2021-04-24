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
        input = """-9"""
        output = """1011"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """123456789"""
        output = """11000101011001101110100010101"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """-1"""
        output = """11"""
        self.assertIO(input, output)

def resolve():
  # 2 進数と同じ様に、1 桁増えるごとに表現できる範囲が 2 倍づつ増えていく。
  # 増え方が、1 が奇数桁だったら負の方向に 2 倍、1 が偶数だったら正の方向に 2 倍になる。
  # -10**9 <= N <= 10**9 なので、最大で 60 桁になるはず。
  # i = 0 ~ 60 まで探索していって、i 桁目を増やした時に N がその表現範囲に入った場合、 i 桁目が 1 になる。
  # N から(-2)^i を引いて再度同じことを行う。
  # これを繰り返すことで最終的に答えが出る・・・はず。
  # 計算回数は 60 * 60/2 くらいなので間に合いそう。
  N = int(input())

  if N==0:
    print(0)
    return
  ans = [0]*120
  max_digit = 0
  while N != 0:
    i=0
    max_val = 0
    min_val = 0
    while True:
      if i%2:
        min_val+=(-2)**i
      else:
        max_val+=(-2)**i
      i+=1
      if min_val<= N and N <= max_val:
        ans[i]=1
        N-=(-2)**(i-1)
        max_digit = max(max_digit, i)
        break
  print(*reversed(ans[1:max_digit+1]), sep="")

resolve()

if __name__ == "__main__":
    unittest.main()
