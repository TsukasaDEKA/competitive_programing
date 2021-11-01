// ==UserScript==
// @name         AlgoMethodPyTestCodeGenerator
// @namespace    http://tampermonkey.net/
// @version      2021.10.19
// @description  It's unittest generator for AtCoeder contest.
// @author       You
// @match        https://algo-method.com/tasks/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// @require https://cdnjs.cloudflare.com/ajax/libs/marked/3.0.7/marked.min.js
// @require http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js
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
  // markdown で書かれた部分を取得する処理
  const propJsonString = $("body").find('#__NEXT_DATA__')[0].textContent;
  const props = JSON.parse(propJsonString).props;
  const markdown = props.pageProps.tasks.body

  // 取得した markdown をパースする処理
  const domparser = new DOMParser();
  const sampleIndex = (markdown.match(/入出力例/) || markdown.match(/サンプル/)).index
  const html = marked(markdown.substr(sampleIndex));

  const doc = domparser.parseFromString(html, "text/html");
  const pre = Array.prototype.slice.call(doc.getElementsByTagName('pre'));
  var inputs = [];
  var outputs = [];
  pre.forEach(function (elem, index) {
    if(index%2==0) inputs.push(elem.innerText);
    else outputs.push(elem.innerText);
  });
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
    return `def resolve():
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
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
from itertools import product
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# resolve()
unittest.main()
`
}

function testCode(){
    const samples = findSamples();
    const inputs = samples["inputs"];
    const outputs = samples["outputs"];
    var result = ""
    for (var i = 0; i < inputs.length; i++) {
        result += `    def test_Sample_Input_${i+1}(self):
        input = """${inputs[i].trimEnd()}"""
        output = """${outputs[i].trimEnd()}"""
        self.assertIO(input, output)\n\n`;
    }
    return result
}

function putTestCodeOnToClipBoard(){
    const code = testCode()
    putStringToClipBoard(header()+code+footer())
    console.log("success");
}

(function() {
  'use strict';
  window.onload = function(){
    var button = document.createElement('button');
    button.style = 'display: inline-block; position: fixed; top: 50px; right: 80px; height: 40px; justify-content: center; align-items: center; background-color: #006666; color: #FFFFF0; border: 8px #002222; z-index: 999; border-radius: 0.7rem; letter-spacing: 0.1em; transition: all 0.3s; padding: 1rem 1rem; text-align: center; vertical-align: middle; font-weight: 700; line-height: 0.7;';
    button.addEventListener ('click', function(){putTestCodeOnToClipBoard();});
    var text = document.createTextNode("テストコード")
    button.appendChild(text);
    document.getElementById("__next").appendChild(button);
  };
})();
