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
        input = """1000 8
1 3 4 5 6 7 8 9"""
        output = """2000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9999 2
1 9"""
        output = """20000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2341 2
1 9"""
        output = """2342"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2349 2
1 9"""
        output = """2350"""
        self.assertIO(input, output)

def resolve():
  # 解説解法
  N, K = map(int, input().split(" "))
  D = [int(x) for x in input().split(" ")]
  can_use = [True]*10
  for d in D: can_use[d] = False

  for n in range(N, 10*N+1):
    temp_n = list(str(n))
    is_ans=True
    for n_s in temp_n:
      if not can_use[int(n_s)]:
        is_ans = False
        break
    if is_ans:
      print(n)
      return
resolve()

if __name__ == "__main__":
    unittest.main()
