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
        input = """FTFFTFFF
4 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """FTFFTFFF
-2 -2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """FF
1 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """TF
1 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """FFTTFF
0 0"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """TTTT
1 0"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # x, y それぞれの軸方向で別々に考えられる。
  # T が入ると使用する軸の方向が切り替わる。
  # 二つの T の間にある F の個数を数えて、T が偶数回出たか奇数回出たかで分けて配列に入れる。
  # この配列の長さを L とすると、それぞれを正にするか負にするかの組み合わせは 2**L 通りあって、
  # 愚直に全部試すと間に合わない。
  # 同じ数字でまとめてみたらどうか。
  # 例えば X 進むという動作が N 個ある場合、取りうる値は N+1 パターンしかない。
  # 8000 個を TT で区切ると
  S = list(input())
  N = len(S)
  G_X, G_Y = map(int, input().split(" "))
  X = []
  Y = []
  is_X = True
  count = 0
  for i in range(N):
    if S[i] == "T":
      if count:
        if is_X: X.append(count)
        else: Y.append(count)
      count = 0
      is_X = not is_X
    else:
      count+=1
  else:
    if count:
      if is_X: X.append(count)
      else: Y.append(count)

  # G_X, G_Y が実現可能かを判定する。
  dp = set()
  if S[0] == "F":
    dp.add(X[0])
    X[0] = 0
  else:
    dp.add(0)
  for x in X:
    temp = set()
    for d in dp:
      temp.add(d+x)
      temp.add(d-x)
    dp = temp
  if G_X not in dp:
    print("No") 
    return

  # G_X, G_Y が実現可能かを判定する。
  dp = set()
  dp.add(0)
  for y in Y:
    temp = set()
    for d in dp:
      temp.add(d+y)
      temp.add(d-y)
    dp = temp
  if G_Y not in dp:
    print("No") 
    return

  print("Yes")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()