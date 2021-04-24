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
    #     input = """11 2"""
    #     output = """3"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """0 4"""
    #     output = """4"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """0 3"""
    #     output = """3"""
    #     self.assertIO(input, output)


    # def test_Sample_Input_4(self):
    #     input = """112 20210213"""
    #     output = """20210436"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_5(self):
    #     input = """-211 1000000000000000000"""
    #     output = """1000000000000000422"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_6(self):
    #     input = """3 5"""
    #     output = """9"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_7(self):
    #     input = """1000000000000000000 1"""
    #     output = """2"""
    #     self.assertIO(input, output)

    def test_Sample_Input_7(self):
        input = """489647926824927166 979295853649854331"""
        output = """2"""
        self.assertIO(input, output)
def resolve():
  # *= -1 と -= 1 円の組み合わせの個数。
  # 重複する可能性がある
  # dp だと間に合わなさそう。O(1) でやりたい
  # 1 円余ってれば反転できる => パターンが 2 倍になる
  # 2 円で行けるとこまで行って反転パターンと、反転してから 2 円で行けるとこまで行って反転パターン
  B, C = map(int, input().split(" "))
  ans = 0 if (C-1)%2 else 1
  if B == 0:
    ans += (C//2)*2
    print(ans)
    return

  ans = 0
  if B > 0:
    l = max(1, B - (C-1)//2)
    r = B + max(0,(C-2))//2
    if B - C//2 <= 0: ans+=1
  else:
    l = B - (C - 1)//2
    r = min(-1, B + max(0,(C-2))//2)
    if -B - (C-1)//2 <= 0: ans+=1

  ans += (abs(r - l) + 1)*2
  # print(l, r, "ans=", ans)
  if B > 0:
    # 0 回反転で端数が出る
    if l > 1 and C%2 == 0: ans+=1
    # 1 回反転で端数が出る
    if (C-1) >= 2 and (C-1)%2 == 0: ans+=1
  else:
    # 0 回反転で端数が出る
    if C%2 == 0: ans+=1
    # 1 回反転で端数が出る
    if r < -1 and (C-1) >= 2 and (C-1)%2 == 0: ans+=1

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
