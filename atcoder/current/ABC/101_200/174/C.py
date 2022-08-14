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
        input = """101"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """999983"""
        output = """999982"""
        self.assertIO(input, output)

def resolve():
  K = int(input())

  # K が偶数だったら存在しない
  if K % 2 == 0 or K % 5 == 0:
    print(-1)
    return True

  L = 9 * K
  if K % 7 == 0:
    L = int(K / 7 * 9)

  target = 10
  for i in range(1, L+1):
    mod_L = target % L
    # print(mod_L)
    if mod_L == 1:
      print(i)
      return True
    target = mod_L*10

  print(-1)


if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
