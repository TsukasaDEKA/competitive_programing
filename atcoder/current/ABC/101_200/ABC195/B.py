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
        input = """100 200 2"""
        output = """10 20"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """120 150 2"""
        output = """14 16"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """300 333 1"""
        output = """UNSATISFIABLE"""
        self.assertIO(input, output)

def resolve():
  A, B, W = map(int, input().split(" "))
  diff = B-A
  W *= 1000

  max_ans = W//A
  dist = W%A
  if (dist+max_ans-1)//max_ans > diff:
    print("UNSATISFIABLE")
    return

  min_ans = (W+B-1)//B
  if max_ans < min_ans:
    print("UNSATISFIABLE")
    return

  print(min_ans, max_ans)

resolve()

if __name__ == "__main__":
    unittest.main()
