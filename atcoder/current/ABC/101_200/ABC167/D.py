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
        input = """4 3
3 2 4 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """6 727202214173249354
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """4 11
2 2 2 2"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  A = [int(x) - 1 for x in input().split(" ")]

  current = 0
  if K < N:
    for i in range(K):
      current = A[current]
    print(current + 1)
    return True
  else:
    history = [False] * N
    load_map = []
    while True:
      load_map.append(current)
      current = A[current]
      if history[current]:
        loop_length = len( load_map[load_map.index(current):] )
        if loop_length == 0:
          print(current + 1)
          return True

        length_to_loop = len( load_map[:load_map.index(current)] )
        additional_way = (K-length_to_loop)%loop_length
        print(load_map[length_to_loop + additional_way] + 1)
        return True
      else:
        history[current] = True

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()