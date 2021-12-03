import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """lower_camel_case"""
        output = """lowerCamelCase"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """_snakeCase_"""
        output = """_snake_case_"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """KLab"""
        output = """KLab"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """_"""
        output = """_"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """a_bc_9a_b"""
        output = """a_bc_9a_b"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """_bcAtest_"""
        output = """a_bc_9a_b"""
        self.assertIO(input, output)

    def test_Sample_Input_7(self):
        input = """__"""
        output = """__"""
        self.assertIO(input, output)

    def test_Sample_Input_8(self):
        input = """sTLN"""
        output = """s_t_l_n"""
        self.assertIO(input, output)

    def test_Sample_Input_9(self):
        input = """T"""
        output = """T"""
        self.assertIO(input, output)

def resolve():
  import re
  def is_camel(S):
    return re.match(r'^_*[a-z][0-9a-z]*([A-Z][0-9a-z]*)*_*$', S)
  def is_underscore(S):
    return re.match(r'^_*[a-z][0-9a-z]*(_[a-z][0-9a-z]*)*_*$', S)
  S = input()
  if is_camel(S):
    T = ""
    for s in S:
      if s.isupper():
        T += "_" + s.lower()
      else:
        T += s
    print(T)
  elif is_underscore(S):
    T = ""
    while S and S[0] == "_":
      T += "_"
      S = S[1:]
    R = ""
    while S and S[-1] == "_":
      R += "_"
      S = S[:-1]
    f = 0
    for s in S:
      if f:
        T += s.upper()
        f = 0
      else:
        if s == "_":
          f = 1
        else:
          T += s
    T += R
    print(T)
  else:
    print(S)
  # import re
  # 具体的な条件が割とめんどくさい。
  # キャメルケースでもアンダースコア区切りの文字列でもない条件をまとめる。
  # - アンダースコアの次に小文字以外が来る。
  # - 先頭と末尾以外にアンダースコアが入っていて、かつ大文字が含まれている。
  # S = input()
  # N = len(S)
  # if N == 1:
  #   print("".join(S))
  #   return

  # # - 大文字が先頭に来る
  # if re.search('^[A-Z]', S) is not None:
  #   print(S)
  #   return

  # # - アンダースコアの次に小文字以外が来る。
  # if S[0] == "_":
  #   if re.search('_[A-Z0-9_]', S[1:]) is not None:
  #     print(S)
  #     return
  # else:
  #   if re.search('_[A-Z0-9_]', S[1:]) is not None:
  #     print(S)
  #     return

  # # - 先頭と末尾以外にアンダースコアが入っていて、かつ大文字が含まれている。
  # if re.search('_', S[1:-1]) is not None and re.search('[A-Z]', S) is not None:
  #   print(S)
  #   return

  # if re.search('_', S[1:-1]) is not None:
  #   ans = S[0] + re.sub("_(.)", lambda x:x.group(1).upper(), S[1:-1]) + S[-1]
  #   print(ans)
  #   return

  # ans = S[0] + re.sub("([A-Z])", lambda x:"_" + x.group(1).lower(), S[1:])
  # print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()