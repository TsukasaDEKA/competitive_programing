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

    def test_入力例_1(self):
        input = """6 3
3
1 2 3
2
3 4
2
5 6"""
        output = """0
1
1
2
-1
-1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
2
1 2
2
2 3
2
3 4"""
        output = """0
1
2
3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 1
3
2 3 4"""
        output = """0
-1
-1
-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """11 5
4
2 6 9 10
3
1 3 8
5
2 4 6 8 10
2
6 7
4
5 6 7 8"""
        output = """0
2
1
2
2
2
2
1
3
2
-1"""
        self.assertIO(input, output)

def resolve():
  # 同じ論文を書いた人同士を全てパスで繋ぐと N*(N-1)//2 本のパスを繋ぐことになるので間に合わない。
  # X >= 1 な高橋数を持った人が存在する時、X-1 の高橋数を持った人が必ず存在する。
  # => 高橋数が小さい順に決めていけば良い。
  # 高橋数 0 の人が書いた論文に載っている人に高橋数 1 を振って行く。
  # 次に、高橋数 1 の人が書いた論文に載っている人に高橋数 2 を振って行く。
  # 次に、高橋数 2 の人が・・・とやっていけばできそう。
  # => BFS の動きと一緒
  # どの人がどの論文を書いたかを知っている必要があり、毎回検索するのは大変なので最初に集計しておく。
  # 一度使った論文はもうチェックしなくていい。(その論文に載っている人は既により小さな高橋数が振られてるので)
  # => フラグで管理しておいて、必要ない場合は飛ばす。
  from collections import deque
  N, M = map(int, input().split(" "))
  # WRITER[p] : p の論文を書いた人
  WRITER = [set() for _ in range(M)]
  # PAPER[w] : w の人が書いた論文
  PAPER = [set() for _ in range(N)]
  for p in range(M):
    _ = input()
    WRITER[p] = set([int(x)-1 for x in input().split(" ")])
    for w in WRITER[p]:
      PAPER[w].add(p)

  # 各著者の高橋数
  T = [-1]*N
  T[0] = 0

  checked_paper = [False]*M
  checked_writer = [False]*N
  checked_writer[0] = True
  nexts = deque()
  nexts.append(0)
  while nexts:
    n = nexts.popleft()
    for p in PAPER[n]:
      if checked_paper[p]: continue
      checked_paper[p] = True
      for w in WRITER[p]:
        if checked_writer[w]: continue
        checked_writer[w] = True
        T[w] = T[n]+1
        nexts.append(w)

  print(*T, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
