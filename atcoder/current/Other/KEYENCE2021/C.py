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
        input = """2 2 3
1 1 X
2 1 R
2 2 R"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 5
2 3 D
1 3 D
2 1 D
1 2 X
3 1 R"""
        output = """150"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5000 5000 10
585 1323 R
2633 3788 X
1222 4989 D
1456 4841 X
2115 3191 R
2120 4450 X
4325 2864 X
222 3205 D
2134 2388 X
2262 3565 R"""
        output = """139923295"""
        self.assertIO(input, output)

def resolve():
  # DP なんだけど非常に厄介。
  # ある空白マスを通る場合 => そのマスが R, D, X それぞれの場合を計算すれば良い。
  # ある空白マスを通らない場合 => それ以外の経路について、3^<空白マスの個数> 分のバリエーションが生まれる。
  # <通らなかった空白マスの個数> = <全体の空白マスの個数> - <その経路を通った時に通過した空白マスの個数>
  # ある経路があった時に、その経路の最終的な個数は 1*(2**<通った空白マスの個数>)*(3**<通らなかった空白マスの個数>) になる。
  # 2**<通った空白マスの個数> を計算するのは簡単。空白マスから遷移してきた時に 2 を掛ければ良い。
  # 3**<通らなかった空白マスの個数> を計算する方法を考える。
  # 最終的に 3**<通らなかった空白マスの個数> を掛けたい。
  # 3**<通らなかった空白マスの個数> = (3**<全体の空白マスの個数>)/(3**<その経路を通った時に通過した空白マスの個数>) なので、
  # 空白マスから遷移してきた時に 1/3 を掛けて、最終的に出てきた数字に (3**<全体の空白マスの個数>) を掛ける。
  # float の計算を毎回やるとズレが出るのと遅くなるので 1/3　の逆元を掛けることにする。
  mod = 998244353
  per3 = (pow(3, mod-2, mod))%mod
  str_to_i = {"R": 1, "D": 2, "X": 3}

  H, W, K = map(int, input().split(" "))
  MAP = [[0]*(W+1) for _ in range(H+1)]
  for h in range(H):
    MAP[h][W] = str_to_i["R"]
  for w in range(W):
    MAP[H][w] = str_to_i["D"]
  for _ in range(K):
    h, w, c = input().split(" ")
    h, w = int(h)-1, int(w)-1
    MAP[h][w] = str_to_i[c]

  ans = [[0]*W for _ in range(H)]
  ans[0][0] = 1
  for h in range(H):
    ans_h = ans[h]
    ans_h_1 = ans[h-1]
    for w in range(W):
      if MAP[h-1][w] == 0: ans_h[w] += (ans_h_1[w]*2*per3)%mod
      elif MAP[h-1][w] & str_to_i["D"]: ans_h[w] += ans_h_1[w]
      if ans_h[w] >= mod: ans_h[w] %= mod
      if MAP[h][w-1] == 0: ans_h[w] += (ans_h[w-1]*2*per3)%mod
      elif MAP[h][w-1] & str_to_i["R"]: ans_h[w] += ans_h[w-1]
      if ans_h[w] >= mod: ans_h[w] %= mod
  ans = (ans[-1][-1]*pow(3, H*W-K, mod))%mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
