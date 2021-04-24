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
        input = """1817181712114"""
        output = """3"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """14282668646"""
        output = """2"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)
    def test_Sample_Input_4(self):
        input = """21"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  S_string = input()
  S_string += "0"
  dists = [0 for _ in range(2019)]
  dists[0] = 1
  for i in range(len(S_string) - 1):
    dists[int(S_string[i:])%2019] += 1

  ans = 0
  for dist in dists:
    ans += dist * (dist - 1) // 2

  print(ans)

if __name__ == "__main__":
    unittest.main()
