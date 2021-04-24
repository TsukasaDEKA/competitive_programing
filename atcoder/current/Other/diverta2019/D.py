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
        input = """8"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000000"""
        output = """2499686339916"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """16"""
        output = """22"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  # N//m と N%m が等しいということは、N%(m+1)==0 になるので、2 ~ logN-1 の数で割っていって、それで見つけた数 -1 を足していけば良い。
  # 2 と N-1 だけ特殊なので後で足す？
  if N<=2:
    print(0)
    return

  ans = N-1
  for i in range(2, int(-(-N**0.5//1))):
    if N%i==0:
      m = N//i-1
      if N%m == N//m: ans+=m

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
