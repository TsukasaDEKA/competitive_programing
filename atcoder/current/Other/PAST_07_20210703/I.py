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
        input = """2
5 0
-5 0
-1 3
2 4"""
        output = """1 -3
-2 -4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
4 4
12 10
12 4
8 7
-4 -2
100 10"""
        output = """1.4 -4.8
0 0
-15 0
75.4 -52.8"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """10
# -40336 -25353
# 25518 98473
# -66200 57666
# 23235 -64774
# 56870 -67151
# -99509 73639
# 39965 -61027
# -54385 -34598
# -57063 14129
# 63186 -88708
# 88770 85106
# -92520 69200"""
#         output = """-8970.87249328212 61817.21737274555
# -75079.28924877638 -74637.35403870217
# -61384.55754506934 -105449.9760881721
# -10508.55928227892 98726.04733711783
# -63915.43362406853 -87648.93490309674
# -84883.41976667292 8062.914405771756
# -43119.58914921946 33307.21406245974
# -77451.63868397648 -121148.543178062
# 88022.56926540422 -62121.98851386775
# -11146.07084342446 90471.08392051774"""
#         self.assertIO(input, output)

def resolve():
  from math import sqrt
  N = int(input())
  Rx, Ry = map(int, input().split(" "))
  Lx, Ly = map(int, input().split(" "))
  MOLES = [[int(x) for x in input().split(" ")] for _ in range(N)]

  # 平行移動量
  Cx, Cy = (Rx+Lx)/2, (Ry+Ly)/2

  # 回転量
  Rx -= Cx
  Ry -= Cy
  Lx -= Cx
  Ly -= Cy
  cos = -Rx/sqrt(Rx**2+Ry**2)
  sin = Ry/sqrt(Rx**2+Ry**2)

  # 全部のホクロに適用
  for i in range(N):
    Mx, My = MOLES[i]
    Mx -= Cx
    My -= Cy
    print(Mx*cos-My*sin, Mx*sin+My*cos)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()