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
        input = """3 2
#.#
.#.
#.#
#.
.#"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 1
....
....
....
....
#"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  A = [[x=="." for x in list(input())] for _ in range(N)]
  B = [[x=="." for x in list(input())] for _ in range(M)]

  for A_i in range(N-M+1):
    for A_j in range(N-M+1):
      matched = True
      for B_i in range(M):
        for B_j in range(M):
          if A[A_i+B_i][A_j+B_j] != B[B_i][B_j]:
            matched = False
            break
          if not matched: break
      
      if matched:
        print("Yes")
        return True
  
  print("No")

if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
