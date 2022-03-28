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
2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1 2 3"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
  # 全探索すると厳しそう。
  # 全部の組み合わせは 2**(N)-1 個ある。
  # セットで存在しなくちゃいけない組み合わせ、セットで存在してはいけない組み合わせがある。
  # 順に、使うことができるかどうかを判定して、2**(セットの個数)-1 すれば良い。
  mod = 998244353
  inf = 10**18+1
  N = int(input())
  F = [int(x)-1 for x in input().split(" ")]

  rev_F = [set() for _ in range(N)]
  for i in range(N): rev_F[F[i]].add(i)

  ans_count = 0
  used = [False]*N
  for i in range(N):
    if used[i]: continue
    if i == F[i]:
      used[i] = True
      ans_count+=1
      continue

    # i を使用できるか判定する。
    left_set = set([i])
    right_set = set()

    temp_i = F[i]

    while True:
      if used[F[temp_i]]: break
      if F[temp_i] in right_set:
        if len(left_set) == len(right_set):
          for j in left_set: used[j] = True
          ans_count+=1
        break
      right_set.add(F[temp_i])
      left_set.add(F[temp_i])
      temp_i = F[temp_i]
    used[i] = True
    # print(i, right_set, left_set)
  print(pow(2, ans_count, mod)-1)

resolve()

if __name__ == "__main__":
    unittest.main()
