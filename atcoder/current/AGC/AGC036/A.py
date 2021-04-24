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
        input = """3"""
        output = """1 0 2 2 0 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100"""
        output = """0 0 10 0 0 10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """311114770564041497"""
        output = """314159265 358979323 846264338 327950288 419716939 937510582"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1000000000000000000"""
        output = """314159265 358979323 846264338 327950288 419716939 937510582"""
        self.assertIO(input, output)

def resolve():
  S = int(input())
  # root S から順に探索していって、ペアを見つける・・・？
  # 数が大きすぎるので間に合わないかも
  # Sが素数の場合、10**9 制約に引っかかるのでこのやり方は無理。
  # 1 点が (0, 0) の時、|x1y2-x2y1| == S であれば条件を満たすので、その線で責めるか。
  limit = 10**9
  P1 = [0, 0]
  P2 = [limit, 1]
  if S%limit == 0:
    P3 = [0, S//limit]
  else:
    P3 = [limit-S%limit, S//limit+1]
  # P3 = [S%limit, S//limit]
  # print(P2[0]*P3[1]-P2[1]*P3[0])
  # print(P2[0]*P3[1], "-", P2[1]*P3[0])
  print(*P1,*P2,*P3)

resolve()

if __name__ == "__main__":
    unittest.main()
