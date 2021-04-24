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
1 2
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
1 2
2 3
2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4
1 2
2 3
4 1
3 4"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 可能性のある箱の個数を求めればいいので、赤いボールを追跡していけば良さそう。
  # 赤いボールだけしか無い状態でその箱からボールをとった時に、その箱には赤いボールが存在しなくなる。 == 取った時に 0 個なら赤いボールの存在フラグを False にする。
  # シミュレーションしていって、存在しうる場所のフラグを立てていくか、カウントを増やしていく感じ？
  # カウントを増やしていく方式 (存在しうる場所を記録しない方式) ではできなさそうなので、フラグを立てていく方式でやる。

  N, M = map(int, input().split(" "))
  X_Y = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]

  boxes = [1]*N
  red_exist = [False]*N
  red_exist[0] = True

  for x, y in X_Y:
    if boxes[x] == 0: continue
    boxes[x]-=1
    boxes[y]+=1
    if red_exist[x]:
      red_exist[y] = True
    # 移動後 0 になるなら False
    if boxes[x] == 0:
      red_exist[x] = False

  print(red_exist.count(True))

resolve()

if __name__ == "__main__":
    unittest.main()