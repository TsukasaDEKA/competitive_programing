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
        input = """3 2
5 1 4
2 3
1 5"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4"""
        output = """338"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 2
100 100 100
3 99
3 99"""
        output = """300"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000"""
        output = """10000000001"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """8 3
1 2 3 4 5 6 7 8
3 7
2 7
3 8"""
        output = """60"""
        self.assertIO(input, output)

from heapq import heapify, heappop, heappush

def resolve():
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  sortedA = sorted(A)
  integraA = [0, sortedA[0]]

  # O[N]
  for i in range(1, N):
    integraA.append(integraA[-1] + sortedA[i])
  # print(integraA)
  # O[M]
  heap_tasks = []
  heapify(heap_tasks)
  for _ in range(M):
    B, C = map(int, input().split(" "))
    heappush(heap_tasks, ((-1)*C, B))
  

  # O[M]
  start_index = 0
  result = integraA[-1]
  for _ in range(M):
    task = heappop(heap_tasks)
    C = (-1) * task[0]
    B = task[1]
    # B が残りよりも多かった場合、残りに合わせる。
    if start_index + B > N:
      B = N - start_index

    if B == 0:
      break

    # print("task =", B, C)
    if sortedA[start_index + B - 1] <= C:
      # 対象範囲の全てが C より小さかったら全て置き換える。
      result += B*C - (integraA[start_index + B] - integraA[start_index])
      start_index += B
      if start_index >= N:
        break
    elif sortedA[start_index] >= C:
      # 対象範囲の全てが C 以上だったら置き換えせずに終了。
      break
    else:
      # 対象範囲の一部が C 未満だったらその部分だけ置き換えて終了 (残りは全て C 以上になることが保証されているので)
      while sortedA[start_index + B - 1] > C:
        B -= 1
      result += B*C - (integraA[start_index + B] - integraA[start_index])
      break
  print(result)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
