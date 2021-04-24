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
        input = """2 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """123 456"""
        output = """435"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """123456789012 123456789012"""
        output = """123456789012"""
        self.assertIO(input, output)
    def test_Sample_Input_4(self):
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
  # A,B <= 10**12 なので愚直に求めていくと間に合わない。
  # 10**12 という事は 2 進数で表すと 40 桁未満なので、これを利用する。
  # A ~ B の xor という事は、f(0, B) xor f(0, A) xor A なので、 f(0, N) がわかれば良い。
  # N = 0b100 の時、f(0, N) = 0b100。
  # N = 0b101 の時、f(0, N) = 0b001。
  # 上記の事から、
  # 「i 桁目が 1 の時、0 ~ i 桁目 を10進数表記に直して奇数だったら、f(0, N)の i 桁目は 0。偶数だったら f(0, N) の i 桁目は 0」がわかる。(本当か？)
  # これで f(0, N) が最大 40 回の計算で求められるので、f(0, B) xor f(0, A) をやれば良い。
  A, B = map(int, input().split(" "))
  def f_base(a):
    ans = a%2 ^ (a>>1)%2
    for i in range(1, len(bin(a))-2):
      # i 桁目が 1 の時 0 ~ i-1 桁目が偶数だったら f(0, a) の i 桁目は 1
      if (a>>i)%2 and (a&~-(1<<i))%2==0:
        ans+=1<<i
    return ans
  def f(a, b):
    if a == 0: return f_base(b)
    return f_base(b) ^ f_base(a-1)

  print(f(A, B))

# resolve()


if __name__ == "__main__":
    unittest.main()
