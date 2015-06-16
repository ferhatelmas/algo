require 'set'
res = [0]
cache = Set.new res
(1..500000).each do |i|
  res << (((n = res[-1] - i) > 0 and !cache.include?(n)) ? n : n + 2*i)
  cache.add res[-1]
end

while (n = gets.to_i) != -1
  puts res[n]
end
