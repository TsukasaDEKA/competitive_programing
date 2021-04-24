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
3
1
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [0]*(N+1)

  for i in range(N):
    A[i+1] = int(input())

  move_count = 0
  next_index = 1
  for _ in range(N):
    move_count += 1
    if A[next_index] == 2:
      print(move_count)
      return True
    elif A[next_index] == 0:
      print(-1)
      return True
    else:
      temp = next_index
      next_index = A[temp]
      A[temp] = 0

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
