gets.to_i.times do |_|
  sum = 0
  i, n = 5, gets.to_i
  while i <= n
    sum += n / i
    i *= 5
  end
  puts sum
end
