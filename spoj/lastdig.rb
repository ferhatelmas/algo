def solve(a, b)
  res = 1
  while b > 0
    res = (res * a) % 10 if b % 2 == 1
    b /= 2
    a = (a**2) % 10
  end
  res
end

gets.to_i.times do |_|
  puts(solve(*gets.split.map{|n| n.to_i}))
end
