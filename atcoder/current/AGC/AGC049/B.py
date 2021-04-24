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
        input = """3
001
100"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
001
110"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
10111
01010"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
100110
001010"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # 以下の 2 種類の操作ができる。
  # 01 の時、1 を左に移動する。
  # 11 の時、1 を 0 にする。
  # なので、1 が増えることはない。
  # 可能な操作は、 1 を 2 個消すのと、 1 を左に移動すること。1 を右に移動することはできない。
  # 1 の個数の差が 2 の倍数じゃない、S で最も右にある 1 よりも更に右に T 上に 1 が存在する場合、一致させることはできない。
  # T から見ていって、最初に T[i] == 1 なる i を見つけたら S[:i] に 1 が含まれてないか確認し、
  # 偶数だったらそれを全部消す。奇数だったら偶数個分全部消して、残った 1 個と S[i:] に含まれる最も左側の 1 を消す。
  # 上記の操作を行った上で S 上で最も左の 1 と T 上で最も左側の 1 をペアにする。
  # 上記の操作を繰り返していく。
  # 途中で操作ができなくなったら -1 出力。全部ペアにできたら操作回数を数える。
  # O(N+N) (S, T の二本分) なので 10**6 で間に合いそう。
  N = int(input())
  S = list(input())
  T = list(input())

  ans = 0
  S_i = 0
  T_i = 0
  while True:
    # T 上の 1 を見つける。
    while T[T_i] != "1":
      T_i += 1
      if T_i >= N:
        # T_i を見終わったら、残りの S 上にある 1 を全て削除できるか確認する。
        while S_i < N:
          if S[S_i] == "1":
            # S 上で 1 を見つけたら削除処理に入る。
            S[S_i] = "0"
            temp_S_i = S_i
            while S[S_i] != "1":
              S_i += 1
              if S_i == N:
                print(-1)
                return
            ans += S_i - temp_S_i
            S[S_i] = "0"
          S_i+=1
          if S_i >= N:
            print(ans)
            return

    # S_i ~ T_i - 1 までの間で、1 を探して消していく。
    while S_i < T_i:
      if S[S_i] == "1":
        # S 上で 1 を見つけたら削除処理に入る。
        S[S_i] = "0"
        temp_S_i = S_i
        while S[S_i] != "1":
          S_i += 1
          if S_i == N:
            print(-1)
            return
        ans += S_i - temp_S_i
        S[S_i] = "0"
      S_i+=1

    # T[T_i] とペアになる 1 を探していく。
    while S[S_i] != "1":
      S_i += 1
      if S_i == N:
        print(-1)
        return
    ans+=S_i - T_i
    S[T_i] = "1"
    S[S_i] = "0"
    T_i+=1
    if T_i >= N:
      print(ans)
      return

# resolve()

if __name__ == "__main__":
    unittest.main()
