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
        input = """4
0 1 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
0 3 2 1 2 2 1"""
        output = """24"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4
0 1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """5
0 1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  N = int(input())
  D = [int(x) for x in input().split(" ")]
  # 出現した数字の数を数える。
  count_D = [0] * N
  for d in D: count_D[int(d)]+=1

  # 根が 1 つ以外だったら 0 を返す。
  if count_D[0]!=1 or D[0]!=0:
    print(0)
    return

  # 後ろから Di == 0 を消していく。
  i = N-1
  while count_D[i] == 0:
    del count_D[i]
    i-=1

  ans = 1
  for i in range(1, len(count_D)):
    if count_D[i] != 0:
      ans *= count_D[i-1]**count_D[i]
      if ans >= mod: ans%=mod
    else:
      # 途中で 0 が見つかったら 0 を返す。
      print(0)
      return
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
