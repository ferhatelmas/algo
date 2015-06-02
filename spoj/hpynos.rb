require 'set'

s, n, c = Set.new, gets.to_i, 0
while not(s.include? n or n == 1)
  s << n
  c += 1
  n = n.to_s.split('').reduce(0){|t, e| t + e.to_i ** 2}
end

puts n == 1 ? c : -1
