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
        input = """3 5 4
11100
10001
00111"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5 8
11100
10001
00111"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 10 4
1110010010
1000101110
0011101001
1101000111"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  popcnt = lambda x: bin(x).count("1")
  # H, W の非対称性をいい感じに使うと良さそう。
  # 水平分割を全パターン試すとして 2**9 = 512 通り、
  # そこから垂直分割を左から順に試していく。
  # 特定区間に K 個存在するかどうかは二次元累積和を使えば判定できる。
  H, W, K = map(int, input().split(" "))
  S = [[int(x) for x in list(input())] for _ in range(H)]
  sumS = [[0]*(W+1) for _ in range(H+1)]
  for h in range(H):
    for w in range(W):
      sumS[h+1][w+1] = S[h][w] + sumS[h+1][w] + sumS[h][w+1] - sumS[h][w]

  ans = 10**8
  for bit in range(1<<(H-1)):
    temp = popcnt(bit)
    cut_line = [0]
    for i in range(H):
      if bit&(1<<i): cut_line.append(i+1)
    cut_line.append(H)
    w_ = 0
    for w in range(1, W+1):
      for i in range(1, len(cut_line)):
        h_ = cut_line[i-1]
        h = cut_line[i]
        if sumS[h][w]-sumS[h_][w]-sumS[h][w_]+sumS[h_][w_] > K:
          temp += 1
          w_ = w-1
          # 切り替え直後に判定して、K を超えるセルがあったら break
          for j in range(1, len(cut_line)):
            h_ = cut_line[j-1]
            h = cut_line[j]
            if sumS[h][w]-sumS[h_][w]-sumS[h][w_]+sumS[h_][w_] > K:
              break
          else: continue
          break
      else: continue
      break
    else:
      if ans > temp:
        ans = temp
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()