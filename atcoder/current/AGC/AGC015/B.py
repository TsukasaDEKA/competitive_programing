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
        input = """UUD"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """UUDUUDUD"""
        output = """77"""
        self.assertIO(input, output)

def resolve():
  # S[0] と S[-1] が それぞれ U, D なので、最大 2 回でどこの階へもいけることが保証されてる。
  # つまり、S[i] == U の場合、 0 ~ i-1 階へは 2 回、 i+1 ~ |S| 解までは 1 回で移動できる。 
  # S[i] == D の場合はその逆。
  S = list(input())
  ans = 2*(len(S)-1)
  for i in range(1, len(S)-1):
    if S[i] == "U":
      ans += i*2 + (len(S)-1-i)
    else:
      ans += i + (len(S)-1-i)*2

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
