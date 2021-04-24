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
        output = """Yes
3
2 1 2
2 3 1
2 2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4"""
        output = """No"""
        self.assertIO(input, output)


    def test_Sample_Input_3(self):
        input = """6"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1"""
        output = """Yes
2
1 1
1 1"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  # 数列かどうか判定する。
  for i in range(1, 600):
    f = i*(i+1)//2
    if N == f: break
    if N < f:
      print("No")
      return

  print("Yes")
  print(i+1)
  ans = [set() for _ in range(i+1)]

  for j in range(i):
    for k in range((j+1)*j//2+1, (j+1)*(j+2)//2+1):
      ans[k-base].add(k)
      ans[j+1].add(k)

  for a in ans:
    print(len(a), *a, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
