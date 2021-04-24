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
        input = """5 3
1 2
3 4
3 1"""
        output = """4"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """4 6
# 1 2
# 2 1
# 1 2
# 2 1
# 1 3
# 2 3
# 2 4"""
#         output = """4"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 10
1 2
2 1
1 2
2 1
1 2
1 3
1 4
2 3
2 4
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 4
3 1
4 1
5 9
2 6"""
        output = """3"""
        self.assertIO(input, output)

import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限

from collections import deque


def resolve():
  N, M = map(int, input().split(" "))
  connections = []
  for _ in range(N):
    connections.append(deque())
  checked = [False] * N
  prev = [None] * N

  for _ in range(M):
    A, B = map(int, input().split(" "))
    A -= 1
    B -= 1
    connections[A].append(B)
    connections[B].append(A)

  max_count = 0
  for i in range(N):
    if checked[i]:
      continue

    checked[i] = True
    count = 1 # 自身が入ってるので 1 から count 開始
    current = i
    # 根に戻ってくるまでループする
    while current != i or len(connections[current]) != 0:
      checked[current] = True
      # 次のノードを見つける
      next_node = connections[current].pop()
      # チェック済みのノードにぶつかった時は next_node を入れ替える。
      while checked[next_node]:
        if len(connections[current]) != 0:
          next_node = connections[current].pop()
        else:
          # チェック済みじゃ無いノードが見つからなかった場合は Break する。
          next_node = None
          break


      # チェックしながら行けるところまで行く
      while next_node is not None:
        prev[next_node] = current
        current = next_node
        # 移動した瞬間に count をインクリメントする。
        count += 1
        checked[current] = True
        # next_node　が見つからなかった場合は Break. 遡る処理に入る。
        if len(connections[current]) == 0:
          break

        next_node = connections[current].pop()
        # チェック済みのノードにぶつかった時は next_node を入れ替える。
        while checked[next_node]:
          if len(connections[current]) != 0:
            next_node = connections[current].pop()
          else:
            # チェック済みじゃ無いノードが見つからなかった場合は Break する。
            next_node = None
            break
      
      # 行き止まりにまで到達してることが保証されているので一旦 1 つ戻る
      if prev[current] is None:
        continue
      current = prev[current]

      # 次の分岐が来るまで遡る
      while len(connections[current]) == 0:
        if prev[current] is not None:
          current = prev[current]
        else:
          break

    max_count = max(count, max_count)
  # print(prev)
  print(max_count)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
