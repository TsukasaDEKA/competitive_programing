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
        input = """2 3 1 2"""
        output = """3.000000 0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2 1 1"""
        output = """2.000000 1"""
        self.assertIO(input, output)

def resolve():
  # 対称性を考えると、必ず 1/2 に分割できることがわかる。
  # また、点が中心にあつ場合のみ、分割方法は複数になって、そうでない場合は一個だけになるはず。
  W, H, x, y = map(int, input().split(" "))
  print((W*H)/2, int(W/2 == x and H/2==y))

resolve()

if __name__ == "__main__":
    unittest.main()
