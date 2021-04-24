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
        input = """6 1
LRLRRL"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """13 3
LRRLRLRRLRLLR"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 1
LLLLLRRRRR"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """9 2
RRRLRLRLL"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
  # 0 ~ K 回の範囲で操作して、幸せな人を増やす。
  # 操作は 「部分列を 180° 反転させる」
  # N<=10**5、K<=10**5 なので、全探索だと多分間に合わない。
  # 現状で幸福な人を数えて、追加で何人幸福にできるか考える。
  # l ~ r に対して操作を行う場合、S[l]==S[r] でなければ幸福である人数は増えない。
  # 例えば ><...>> の場合、<...> 部分を反転させても幸福な人の数は変わらない。
  # <>...>< or ><...<> のような状態を探して操作を行うのが最も効率が良い。

  # これは l == r の時も変わらない。(><> で 真ん中の人だけ反転で >>> になって幸福 +2)
  # 色々考えたけど、LRL or RLR (中の R or L は複数可能) を探して、見つけたら幸福 +2 しながら幸福な人を探すというのを繰り返していけば良さそう。
  # バグらせたので "現状幸福な人" と "幸福にできる人" を分けて計測する。 
  N, K = map(int, input().split(" "))
  S = list(input())
  happy_count = 0
  anker_index = None
  for i in range(N):
    if i>0:
      if S[i] == "L" and S[i-1] == "L": happy_count+=1
    if i<N-1:
      if S[i] == "R" and S[i+1] == "R": happy_count+=1

  # print(happy_count)
  i=0
  while i < N-1:
    if S[i] != S[i+1]:
      if anker_index is None:
        anker_index = i+1
      else:
        happy_count += 2
        # 顔反転。要らないかも。
        # reversed_face = "L" if S[i]=="R" else "R"
        # for j in range(anker_index, i+1): S[j]=reversed_face
        K-=1
        if K<=0: break
        anker_index = None
    i+=1

  # print(happy_count)
  if anker_index is not None and K>0:
    happy_count+=1

  # print(*S, sep="")
  print(happy_count)

resolve()


if __name__ == "__main__":
    unittest.main()
