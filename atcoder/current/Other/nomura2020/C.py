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
0 1 1 2"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
0 0 1 0 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
0 3 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
1 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """10
0 0 1 1 2 3 5 8 13 21 34"""
        output = """264"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  if N == 0 and A[0] != 1:
    print(-1)
    return True
  min_maxs = [0] * len(A)
  min_maxs[len(A)-1] = [A[-1], A[-1]]

  for index in reversed(range(len(A)-1)):
    min_maxs[index] = [min_maxs[index+1][0] // 2 + A[index], min_maxs[index+1][1] + A[index]]

  result = 1
  recent = 1
  for index in range(1, len(A)):
    num_of_node = (recent - A[index-1]) * 2
    if num_of_node < min_maxs[index][0]:
      print(-1)
      return True
    
    result += min(num_of_node, min_maxs[index][1])
    recent = min(num_of_node, min_maxs[index][1])

  print(result)

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()
