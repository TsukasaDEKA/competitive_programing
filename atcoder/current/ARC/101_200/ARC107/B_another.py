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

    # def test_Sample_Input_1(self):
    #     input = """2 1"""
    #     output = """4"""
    #     self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 1"""
        output = """16"""
        self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """2525 -425"""
    #     output = """10314607400"""
    #     self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  ans = 0
  for a in range(1, N+1):
    a_count = 0
    for b in range(1, N+1):
      for c in range(1, N+1):
        for d in range(1, N+1):
          if a+b-c-d == K:
            a_count += 1
            ans += 1
    # print(a, ":", a_count)
  print(ans)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
