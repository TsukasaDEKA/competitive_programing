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
        input = """3 1 4
2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 3
1 2
1 3
2 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 3 100
1 2
4 5
2 3"""
        output = """428417047"""
        self.assertIO(input, output)


def resolve():
  mod = 998244353
  N, M, K = map(int, input().split(" "))

  INVALID_PATH = [[x] for x in range(N)]
  for _ in range(M):
    U, V = [int(x)-1 for x in input().split(" ")]
    INVALID_PATH[U].append(V)
    INVALID_PATH[V].append(U)

  field = [[0]*N for _ in range(K+1)]
  field[0][0] = 1

  for k in range(1, K+1):
    field_k_1 = field[k-1]
    field_k = field[k]
    sum_ = sum(field_k_1)

    for n in range(N):
      temp_sum = sum_
      for i in INVALID_PATH[n]:
        temp_sum -= field_k_1[i]

      field_k[n] = temp_sum
      field_k[n]%=mod
    # if current_sum > mod: current_sum%=mod
  # print(*field, sep="\n")
  print(field[-1][0])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()