// ==UserScript==
// @name         AtCoderPyTestCodeGenerator
// @namespace    http://tampermonkey.net/
// @version      2021.06.26
// @description  It's unittest generator for AtCoeder contest.
// @author       You
// @match        https://atcoder.jp/contests/*/tasks/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

function putStringToClipBoard(str) {
  var listener = function(e){
      e.clipboardData.setData("text/plain" , str);
      // 本来のイベントをキャンセル
      e.preventDefault();
      // 終わったら一応削除
      document.removeEventListener("copy", listener);
  }

  // コピーのイベントが発生したときに、クリップボードに書き込むようにしておく
  document.addEventListener("copy" , listener);

  // コピー
  document.execCommand("copy");
}

function findSamples(){
    const inputPattern = "入力例 ";
    const outputPattern = "出力例 ";
    var inputs = [];
    var outputs = [];
    var i = 0
    $('section').each(function(index, _){
        if($('section').eq(index).find('h3').text().indexOf(inputPattern) === 0){
            i+=1
            inputs.push($('section').eq(index).find('pre').text());
        };
        if($('section').eq(index).find('h3').text().indexOf(outputPattern) === 0){
            outputs.push($('section').eq(index).find('pre').text());
        };
    })

    return {inputs: inputs, outputs: outputs};
}

function header(){
    return `import sys
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
        self.assertEqual(out, output)\n\n`
}

function footer(){
    return `import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
from itertools import product
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
import numpy as np
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def resolve():
  inf = 10**18+1
  N = int(input())
  N, K = map(int, input().split(" "))
  A = [[int(x)+i, i-int(x)] for i, x in enumerate(input().split(" "))]
  A = [int(x) for x in input().split(" ")]
  A = [int(input()) for _ in range(N)]
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  S = list(input())
  S_map = [list(input()) for _ in range(H)]

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()`
}

function testCode(){
    const samples = findSamples();
    const inputs = samples["inputs"];
    const outputs = samples["outputs"];
    var result = ""
    for (var i = 0; i < inputs.length; i++) {
        result += `    def test_Sample_Input_${i+1}(self):
        input = """${inputs[i].trimEnd()}"""
        output = """${outputs[i].trimEnd()}"""\n\n`;
    }
    return result
}

function putTestCodeOnToClipBoard(){
    const code = testCode()
    putStringToClipBoard(header()+code+footer())
    console.log("success");
}

(function() {
    jQuery("span.h2").append('<a><h4>テストコード</h4></a>').on("click",  function(){
        putTestCodeOnToClipBoard()
    });
})();