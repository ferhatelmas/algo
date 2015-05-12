gets.to_i.times do |_|
  i, j, n = 1, 1, gets.to_i
  while i <= n
    j, i = i * j, i + 1
  end
  puts j
end
