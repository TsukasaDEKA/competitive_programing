
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

    def test_入力例_1(self):
        input = """5 3"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 100"""
        output = """0"""
        self.assertIO(input, output)

    # def test_入力例_3(self):
    #     input = """99999 1000000000000000000"""
    #     output = """84563"""
    #     self.assertIO(input, output)

    # def test_入力例_4(self):
    #     input = """0 1000000000000000000"""
    #     output = """0"""
    #     self.assertIO(input, output)

def resolve():
  # ダブリングの練習をする。
  M=10**2
  n,k=map(int,input().split())
  e=k.bit_length()
  D=[[0]*M for _ in range(e)]
  for i in range(M):
    D[0][i]=(i+sum(map(int,str(i))))%M
  for i in range(e-1):
    for j in range(M):
      D[i+1][j]=D[i][D[i][j]]
  i=0
  while k:
    if k%2: n=D[i][n]
    k//=2
    i+=1
  for d in D:
    print(*d)
  print(n)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
