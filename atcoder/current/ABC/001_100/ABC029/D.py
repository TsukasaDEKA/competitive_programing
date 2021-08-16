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
        input = """12"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """345"""
        output = """175"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """999999999"""
        output = """900000000"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """309"""
        output = """161"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """111"""
        output = """36"""
        self.assertIO(input, output)

def resolve():
  # N 以下の数字で 1 の桁に 1 が含まれる数は 末尾を 1 で固定して他の数字を自由に変更した数だけ存在する。
  # なので、N//10+1 個存在するはず。(+1 は 末尾 1 以外の数字が全部 0 だった場合)
  # 重複は弾く必要あるか・・・？他の桁の 1 はカウントに入れてないから重複はない。

  # 以下の 3 パターンが考えられる。
  # i 桁目が 0 の時、i 桁目を 1 に固定してかつ < N を満たすようにするには
  # i より上位桁部分は N//(10**i) よりも小さくなくてはいけない。
  # i 桁目より下位桁は 0 ~ 9 の間で動かせる。

  # i 桁目が 1 の時 、i 桁目を 1 に固定してかつ < N を満たすようにするには 
  # i より上位桁部分は N//(10**i) 以下である必要がある。
  # i 桁目より下位桁は上位桁が N//(10**i) の場合は N%(10**i) 個の場合数があり、
  # 上位桁が N//(10**i) 未満の場合は下位桁は 0 ~ 9 の間で動かせる。

  # i 桁目が 1 より大きい時、i 桁目を 1 に固定してかつ < N を満たすようにするには 
  # i より上位桁部分は N//(10**i) 以下である必要がある。
  # 上位桁が N//(10**i) 未満の場合は下位桁は 0 ~ 9 の間で動かせる。

  N = int(input())
  N_digits = []
  temp = N
  while temp > 0:
    N_digits.append(temp%10)
    temp//=10

  # 各桁を見ていく
  ans = 0
  M = len(N_digits)
  for i in range(M):
    # 下位桁を自由に動かせるパターン
    upper = N//(10**(i+1))
    if N_digits[i] > 1: upper+=1
    ans += upper*(10**i)

    # 下位桁を自由に動かせないパターン
    if N_digits[i] == 1:
      ans += N%(10**i)+1
 
    # ↓の書き方の方がシンプル？
    # if N_digits[i] == 0:
    #   ans += N//(10**(i+1))*(10**i)
    # elif N_digits[i] == 1:
    #   ans += N//(10**(i+1))*(10**i) + N%(10**i)+1
    # else:
    #   ans += (N//(10**(i+1))+1)*(10**i)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()