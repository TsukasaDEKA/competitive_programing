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
        input = """6 2 1001"""
        output = """1369"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000 2 16"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10000000000 10 99959"""
        output = """492443256176507"""
        self.assertIO(input, output)

def resolve():
  N, X, M = map(int, input().split(" "))
  checked = [False] * M
  val = X
  ans = 0
  val_list = []

  base = M
  for i in range(N):
    if checked[val] != False:
      loop_start_index = checked[val]
      loop_vals = val_list[loop_start_index:]
      loop_val = sum(loop_vals)
      loop_length = len(val_list[loop_start_index:])
      
      if loop_length != 0:
        ans += ((N - i) // loop_length) * loop_val

        for i in range(((N - i) % loop_length)):
          ans += loop_vals[i]
      break
    ans += val
    checked[val] = i
    val_list.append(val)

    val*=val
    if val >= base:
      val %= base


  print(ans)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
