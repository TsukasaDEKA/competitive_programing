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
        input = """2
FLIP
2
2 0 0
1 1 4"""
        output = """LPFI"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4"""
        output = """ILPF"""
        self.assertIO(input, output)

def resolve():
  #このdefが怪しい？？？
  def t1(S, A, B):

    Sa = S[A]
    Sb = S[B]
    # 考え方自体はいいけど、これをやると　くっつけたり切り取ったりの処理で時間が取られる。
    # 入れ変えたいなら↓で十分
    # S を string で持ってるとこの操作ができないので、一度 list にしておく。
    S[A] = Sb
    S[B] = Sa
    # if A == 0: # <= ここを A == 0 にする。
    #     S0 = ""
    # else:
    #     S0 = S[0:A]
    # S1 = S[A+1:B]
    # if B == len(S):
    #     S2 = ""
    # else:
    #     S2 = S[B+1:len(S)]
    # # print(S, S0, Sb, S1, Sa, S2)

    # S = S0 + Sb + S1 + Sa + S2
    return S

  def t2(S):
    #S = S[N:2N]+S[0:N] Nがだめっぽい
    n = len(S)
    S1 = S[:n//2]
    S2 = S[n//2:]
    S = S2+S1
    return S

  N = int(input())
  # S = input()
  # 今回は一文字の入れ替えをするので、list でやると便利
  S = list(input())
  Q = int(input())
  T = [list(map(int, input().split())) for i in range(Q)]

  k = 0
  for i in range(Q):
    if T[i][0] == 1:
      Ta = T[i][1]-1
      Tb = T[i][2]-1
      #交換
      if k == 1:
        if Ta < N:
          Ta += N
        else:
          Ta -= N
        if Tb < N:
          Tb += N
        else:
          Tb -= N
        #Tb<Taなので
        # 上で N を足しひきしてるので、 Tb < Ta が成り立つか保証されない。
        # min(Tb, Ta), max(Tb, Ta) みたいにするとうまくいく。
        # S = t1(S, Tb, Ta)
        S = t1(S, min(Tb, Ta), max(Tb, Ta)) 
      else:
        #Ta<Tbなので
        S = t1(S, Ta, Tb)
    else:
      #前後入れ替え
      if k == 0:
        k += 1
      else:
        k -= 1

  if k == 1:
    S = t2(S)
  # 一度 list にしたので、"".join(S) でくっつけて出力する。
  # print(S)
  print("".join(S))
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
