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
        input = """1000 8
1 3 4 5 6 7 8 9"""
        output = """2000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9999 2
1 9"""
        output = """20000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2341 2
1 9"""
        output = """2342"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2349 2
1 9"""
        output = """2350"""
        self.assertIO(input, output)

def resolve():
  # 頭から見ていって、同じ数が作れないか試す。
  # もし無理だったら、その桁をその桁より大きい数字に置き換えられないか試す。
  # 無理だったらそこから一つづつ戻っていって、その桁をその桁より大きい数字に置き換えられないか試す。
  # 置き換えることができたら、それより右側の桁を全て使用できる数字の最小値に置き換える。
  # 置き換えることができなかったら、先頭に使用できる数字の最小値(0を除く)+使用できる数字の最小値*Nの桁数出力する。
  N, K = map(int, input().split(" "))
  D = [int(x) for x in input().split(" ")]
  can_use = [True]*10
  for d in D: can_use[d] = False
  min_num = 0
  for i in range(10):
    if can_use[i]:
      min_num=i
      break
  N = [int(x) for x in list(str(N))]
  ans = [0]*len(N)

  # 頭から見ていって、同じ数が作れないか試す。
  for i in range(len(N)):
    if can_use[N[i]]:
      ans[i]=N[i]
      continue
    else:
      # その桁をその桁より大きい数字に置き換えられないか試す。
      for j in reversed(range(i+1)):
        for k in range(N[j]+1, 10):
          if can_use[k]:
            ans[j]=k
            # 置き換えることができたら、それより右側の桁を全て使用できる数字の最小値に置き換える。
            for l in range(j+1, len(ans)):
              ans[l]=min_num
            print(*ans, sep="")
            return
      # 置き換えることができなかったら、先頭に使用できる数字の最小値(0を除く)+使用できる数字の最小値*Nの桁数出力する。
      for j in range(1, 10):
        if can_use[j]:
          print(j, str(min_num)*len(N), sep="")
          return
  print(*ans, sep="")

resolve()

if __name__ == "__main__":
    unittest.main()
