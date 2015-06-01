while true
  a, b = gets.split.map{|n| n.to_i}.sort
  break if a == -1 and b == -1
  puts b / (a + 1) + (b % (a + 1) == 0 ? 0 : 1)
end
