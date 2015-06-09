gets.to_i.times do |_|
  n = gets.to_i
  puts((3 * n * (n+1) / 2 - n) % 1000007)
end
