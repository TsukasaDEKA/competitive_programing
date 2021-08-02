from collections import defaultdict
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

    # def test_Sample_Input_1(self):
    #     input = """13 2"""
    #     output = """5"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """100 80"""
    #     output = """99"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """1000000000000000000 1000000000"""
    #     output = """841103275147365677"""
    #     self.assertIO(input, output)

def resolve():
  from collections import deque

  # 0 ~ 9 までの数字を最大 9 個並び替えて、積が K より大きくなるものを削除する。
  # 10 種類の数字から 9 個選ぶ組み合わせは何パターンあるか。=> https://manabitimes.jp/math/1101
  # 92,378 パターンある。
  # そのパターンから 積が 9 を超えないものを選んで、さらに N を超えないパターンを選び出す？
  # 前から順に条件を満たしながら決めていって、DP かな。
  # 途中で 0 を選んだら後ろは自由に決めれる。
  # 深さ優先探索していって、値が 0 になった時点で pow(10, 残りの桁数) を答えにたす。
  N, K = map(int, input().split(" "))
  listN = [int(x) for x in list(str(N))]
  lenN = len(str(N))
  numbers = list(range(10))

  ans = 0
  # 一桁めを入れておく。
  nexts = deque()
  for n in range(1, 10):
    for r in range(lenN):
      if n*pow(10, r) > N: continue
      if n > K: continue
      nexts.append((n*pow(10, r), n, r))

  while nexts:
    val, prd, rank = nexts.pop()
    if prd == 0 or rank == 0:
      if prd > K: continue
      ans += pow(10, rank)
      print(val)
      continue

    for i in range(10):
      if val+i*pow(10, rank-1) > N: continue
      if prd*i > K: continue
      print((val+i*pow(10, rank-1), prd*i, rank-1))
      nexts.append((val+i*pow(10, rank-1), prd*i, rank-1))
  print(ans)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()