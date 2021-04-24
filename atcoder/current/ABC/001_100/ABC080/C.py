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
        input = """1
1 1 0 1 0 0 0 1 0 1
3 4 5 6 7 8 9 -2 -3 4 -2"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1"""
        output = """-2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1 1 1 1 1 1 0 0 1 1
0 1 0 1 1 1 1 0 1 0
1 0 1 1 0 1 0 1 0 1
-8 6 -2 -8 -8 4 8 7 -6 2 2
-9 2 0 1 7 -5 0 -2 -6 5 5
6 -6 7 -9 6 -5 8 0 -9 -7 -7"""
        output = """23"""
        self.assertIO(input, output)

def resolve():
  # 出店する時間帯の選び方は 2**10-1 個(大体 10**3 くらい)ある。
  # ある時間帯の選び方を選んだ時の計算量は 10*100 の計算量。総当たりすると 10**6 より少し多いくらいなのでいけるか？
  # メモ化すればかなり計算量減らせそう。BIT DP？ 
  inf = 10**10+1
  N = int(input())
  F = [[int(x) for x in input().split(" ")] for _ in range(N)]
  P = [[int(x) for x in input().split(" ")] for _ in range(N)]

  ans = -1*inf
  for i in range(1, 2**10):
  # for i in range(1, 2**3):
    temp_ans = 0
    for j in range(N):
      k = 0
      count_store=0
      temp_i = i
      while temp_i > 0:
        if temp_i%2==1 and F[j][k]:
          count_store+=1
        temp_i>>=1
        k+=1
      temp_ans+=P[j][count_store]
    ans=max(ans, temp_ans)

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
