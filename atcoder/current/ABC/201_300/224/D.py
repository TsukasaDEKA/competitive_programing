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
        input = """5
1 2
1 3
1 9
2 9
3 9
3 9 2 4 5 6 7 8"""
        output = """5"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """5
# 1 2
# 1 3
# 1 9
# 2 9
# 3 9
# 1 2 3 4 5 6 7 8"""
#         output = """0"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """12
# 8 5
# 9 6
# 4 5
# 4 1
# 2 5
# 8 9
# 2 1
# 3 6
# 8 7
# 6 5
# 7 4
# 2 3
# 1 2 3 4 5 6 8 7"""
#         output = """-1"""
#         self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """12
# 6 5
# 5 4
# 4 1
# 4 7
# 8 5
# 2 1
# 2 5
# 6 9
# 3 6
# 9 8
# 8 7
# 3 2
# 2 3 4 6 1 9 7 8"""
#         output = """16"""
#         self.assertIO(input, output)

def resolve():
  from collections import deque
  # 閉路があって、そこに空が含まれる場合、巡回できる
  # 空のマスに仮のコマを置いて、それを動かす (行き先と交換する) イメージでやってみる？
  # 閉路を探して、それに含まれるかどうかを判定する。
  # 仮コマを閉路内部まで移動させる。
  # その時点で閉路に含まれないマスをチェックして、正しい状態になっているか確認する。
  # 正しくない場合はそれで終わり。
  # 正しい場合は閉路内で動かす。
  # 仮コマを動かして最終的に 9 に移動できるかを考える。
  # 全てのコマを動かした時にすれ違いが発生しないかどうかを考える。
  # 全ての経路を考えると無理。
  # 
  N = 9
  M = int(input())
  EDGES = [[] for _ in range(N+1)]
  for _ in range(M):
    u, v = [int(x) for x in input().split(" ")]
    EDGES[u].append(v)
    EDGES[v].append(u)

  P = [int(x) for x in input().split(" ")]
  

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()