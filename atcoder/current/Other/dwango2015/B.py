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

    def test_入力例1(self):
        input = """2525"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1251251252525"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """25225"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """252252252252252252"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """20061212"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  S = input()

  if len(S) < 2:
    print(0)
    return True

  ans = 0
  i = 0
  while i + 1 < len(S):
    count = 0
    while i + 1 < len(S):
      if S[i:i+2] == "25":
        count+=1
        i+=2
        if i + 1 >= len(S):
          ans+=(count*(count+1))//2
          break
      else:
        ans+=(count*(count+1))//2
        i+=1
        break

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
