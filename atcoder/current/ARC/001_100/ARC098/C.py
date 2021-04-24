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
        input = """5
WEEWW"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12
WEWEWEEEWWWE"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
WWWWWEEE"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
E"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # E と W で区間和をとると、i 番目の人をリーダーにした時の振り向く人数が O(1) で出せる。
  # 全体で O(N)
  N = int(input())
  S = list(input())
  E = [0]*(N+1)
  W = [0]*(N+1)
  for i in range(N):
    if S[i]=="E":
      E[i+1] = E[i]+1
      W[i+1] = W[i]
    else:
      E[i+1] = E[i]
      W[i+1] = W[i]+1
  print(min(E[-1] - E[i+1] + W[i] for i in range(N)))

resolve()


if __name__ == "__main__":
    unittest.main()
