=begin
最強の文字列
ぷれ君とぺん君は、丁度2枚のチタンを使って文字列Sを強化したいと思っています。
強化されてできた最強の文字列は、この星を守るDEKA君のサイボーグ化に使われます。
/D.*E.*K.*A/ にマッチする部分をチタン1枚で強化できます。また、2枚のチタンによる強化部分に重なりがあってはいけません。
最大何文字をチタンで強化できるか求めてください。
制約
Sは長さが1以上200000以下のA-Zのみで構成された文字列
入力
S
出力
答えを整数で出力・チタンを丁度2枚使うことができない場合は-1を出力
入力例1
DEKAKDAEKDEKA
出力例1
12
DEKAとDAEKDEKAの部分をチタンで強化することで、最大12文字強化できます
入力例2
DEKAEKA
出力例2
-1
チタン1枚でしか強化できないので、-1を出力します
=end

def red(s, color: nil)
  "\e[31m#{s}\e[m"
end

def green(s)
  "\e[32m#{s}\e[m"
end

patterns = [
  [
    [
      'EKA*',
      'D', 'KA*', 'DEK*', 'E', 'EK*', 'K', 'EKA*', 'A',
      'EK*',
      'D', 'DEK*', 'E', 'EK*', 'K', 'EKA*', 'DE*', 'A',
      'DEK*'
    ], ->(c) { c.values_at(*1..4, *6..9).sum + 8 }
  ],
  [
    [
      'EKA*',
      'D', 'KA*', 'DEK*', 'E', 'EK*', 'K', 'EKA*', 'A',
      'EK*',
      'D', 'DEK*', 'E', 'EK*', 'K', 'EKA*', 'A',
      'EK*',
      'D', 'DEK*', 'E', 'EK*', 'K', 'EKA*', 'DE*', 'A',
      'DEK*'
    ], ->(c) { [c.values_at(*1..8, *10..13).sum, c.values_at(*1..4, *6..13).sum].max + 12 }
  ],
  [
    [
      'EKA*',
      'D', 'DEKA*', 'E', 'DEKA*', 'K', 'DEKA*', 'A',
      'D', 'DEKA*', 'E', 'DEKA*', 'K', 'DEKA*', 'A',
      'DEK*'
    ], ->(c) { c.values_at(*1..6).sum + 8 }
  ],
  [['EKA*', 'D', 'KA*', 'DEK*', 'E', 'EK*', 'K', 'EKA*', 'DE*', 'A', 'DEK*'], ->(_c) { -1 }],
  [['EKA*', 'DEK*'], ->(_c) { -1 }]
]
def create(pattern, counts)
  others = [*'A'..'Z'] - 'DEKA'.chars
  counts = counts.dup
  pattern.map do |p|
    if p.size == 1
      p
    else
      chars1 = p.delete('*').chars
      chars2 = p.include?('*') ? others : chars1
      counts.shift.times.map { (rand < 0.5 ? chars1 : chars2).sample }.join
    end
  end.join
end
require 'open3'
require 'timeout'
if ARGV.empty?
  puts 'ARGV required.'
  puts 'try `ruby test.rb python ./Main.py`'
  exit
end
def test(s, answer)
  t = Time.now
  io, ans = nil
  Timeout.timeout(2) do
    io = IO.popen ARGV, 'r+'
    io.puts s
    ans = io.gets
    io.close
  end
  stat = ans.to_i == answer ? 'AC' : 'WA'
  puts "#{stat == 'AC' ? stat : red(stat)} #{((Time.now - t)*1000).round}ms"
  stat
rescue => e
  Process.kill :TERM, io.pid rescue nil if io
  stat = e.is_a?(Timeout::Error) ? 'TLE' : 'RE'
  puts "#{red stat} #{((Time.now - t)*1000).round}ms"
  stat
end

srand 0
status = []
status << test('DEKADEKA', 8)
status << test('DEKAKDAEKDEKA', 12)
status << test('DEKAEKA', -1)
[2000, 200000].each do |size|
  patterns.each do |pattern, ans_proc|
    embed_size = pattern.count {|p| p.size >= 2 }
    rands = (0..embed_size).map {|i| 2**i - 1 }
    scale = (size - pattern.size).fdiv rands.sum
    counts_base = rands.map {|n| (n * scale).floor }
    4.times do
      counts = counts_base.shuffle
      s = create pattern, counts
      ans = ans_proc.call counts
      status << test(s, ans)
    end
  end
end

if status.uniq == ['AC']
  puts green('AC!')
else
  class Array
    unless method_defined? :tally
      def tally; group_by(&:itself).transform_values(&:size); end
    end
  end
  puts red(status.tally.inspect)
end
