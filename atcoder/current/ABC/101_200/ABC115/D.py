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
        input = """2 7"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """50 4321098765432109"""
        output = """2160549382716056"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """50 51"""
        output = """1"""
        self.assertIO(input, output)

def count_patty(L, X):
  # レベル L バーガーにおける X 枚までのパティの枚数を返す。
  if X > 2*(-3+2**((L-1)+2))+2: return 2**(L+1)-1
  if X > -3+2**((L-1)+2)+1: return 2**L + count_patty(L-1, X-(-3+2**((L-1)+2)+2))
  if X > 1: return count_patty(L-1, X-1)
  return 0

def resolve():
  # パティの枚数は 2^(L+1)-1 枚、総枚数は -3+2^(L+2) である。
  # レベル N のパンを左から見ていって、X-1 >= -3+2^((N-1)+2) の時、食べるパティの枚数は 2^((N-1)+1)-1 枚増える。
  # X-1 < -3+2^((N-1)+2) の時 X-1 > = -3+2^(((N-1)-1)+2) であれば食べるパティの枚数は 2^(((N-1)-1)+1)-1 枚増える。
  # ・・・といったように再帰的にパティの枚数を求めていけば最終期にパティの枚数は求まるはず。
  # 計算量は O(N) より少し多いくらいか。
  N, X = map(int, input().split(" "))
  print(count_patty(N, X))

resolve()


if __name__ == "__main__":
    unittest.main()
