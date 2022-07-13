1//1 if 0 else 1;"""
/*"""
import sys
import subprocess
import unittest
from io import StringIO

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        p = subprocess.Popen(
            ['ts-node', __file__],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, error = p.communicate(input=input.encode())
        self.assertEqual(error.decode().strip(), "")
        self.assertEqual(out.decode().strip(), str(output))

    def test_Sample_Input_1(self):
        input = """4 10"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 8"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
  unittest.main()
"""*/
import * as fs from 'fs';

const input = fs.readFileSync("/dev/stdin", "utf8").split("\n");
const [a, b] = input[0].split(" ").map(x=> Number(x));

const main = () => {
  let count = 0;
  let current = 1;
  while (current < b) {
    count += 1;
    current += a-1;
  }
  console.log(count);
};

main();
//"""