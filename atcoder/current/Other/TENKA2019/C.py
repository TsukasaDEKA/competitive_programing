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
        input = """3
#.#"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
#.##."""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9
........."""
        output = """0"""
        self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """9
# ##.#....."""
#         output = """1"""
#         self.assertIO(input, output)


def resolve():
  inf = 10**10+1
  N = int(input())
  S = [ x=="." for x in list(input())]
  # 最終的に白(0~N個)+黒(0~N個)の関係になれば良くて、そうするためには最小何個の石の色を変更する必要があるか考える。
  # 白黒のそれぞれの累積和を取って、i 番目移行の白石と i 番目より手前の黒石の数を数えて、最小値を出す。
  integral_W = [0]*(N+1)
  integral_B = [0]*(N+1)
  for i in range(N):
    if S[i]:
      integral_W[i+1] = integral_W[i]+1
      integral_B[i+1] = integral_B[i]
    else:
      integral_W[i+1] = integral_W[i]
      integral_B[i+1] = integral_B[i]+1

  ans = inf
  for i in range(N+1):
    ans = min(ans, integral_B[i]+integral_W[-1]-integral_W[i])
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
