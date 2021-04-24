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

#     def test_Sample_Input_1(self):
#         input = """4
# 1
# 3
# 2
# 4"""
#         output = """2"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """6
# 3
# 2
# 5
# 1
# 4
# 6"""
#         output = """4"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """8
# 6
# 3
# 1
# 2
# 7
# 4
# 8
# 5"""
#         output = """5"""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4
4
3
2
1"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # O(N) とか O(NlogN)とかで解かないと厳しい。
  # 例 1 
  # [0, 2, 1, 3]
  # これは 1 を先頭 => 0 を先頭か、2 を末尾 => 3 を末尾のどちらかの操作をする。
  # [1, 2, 0, 3] スタートだったら？
  # 0 を先頭に持っていけば終わり。操作 1 回で終わる。
  # 例 2
  # [3, 2, 5, 1, 4, 6]
  # 2, 1, 5, 6 を操作。
  # 4, 3, 2, 1 を操作でもいける。 
  # 既に順番に並んでるやつは触らなくていい
  # 間にあるやつを引っこ抜いて先頭か末尾に回す
  # 逆に、間に何かの数字を突っ込む動作 (例えば例 2 の 4, 6 の間に 5 を入れるとか) は出来ないので、
  # どちらかは先頭に動かす必要がある。
  # 適切な順番に操作すれば、最大 N-1 回の操作で終わるはず。
  # => 1 個だけ触らないで他のを適切な順番で操作すれば良いので。
  # 前から見ていって、順番を ~~乱している~~ 乱していないやつを数えて、そいつの個数だけ数えればいい。
  # 例 3
  # [6, 3, 1, 2, 7, 4, 8, 5]
  # 触らないのは [1, 2] or [3, 4, 5] or [6, 7, 8] のどれかで
  # [3, 4, 5] or [6, 7, 8] のどちらかを触らないことにすると 8-5 = 3
  # 左から順に取っていって、取った数字が P(i) だとすると、 
  # P(i)-1 が既に取った中に含まれてたら index を上げるようにする。
  # 6 とる => 6 に 1 を入れる。3 とる 3 に 1 を入れる。 1 とる 1 に 1 を入れる
  # 2 とる => 1 に既に 1 が入ってるので、2 に 1+1 を入れる
  # 7 とる => 6 に既に 1 が入ってるので、7 に 1+1 を入れる
  # いけそう。
  N = int(input())
  P = [int(input())-1 for _ in range(N)]
  history = [0]*N
  for p in P:
    if p == 0:
      history[p] = 1
      continue
    history[p] = history[p-1]+1
  print(N-max(history))

resolve()


if __name__ == "__main__":
    unittest.main()
