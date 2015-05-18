while (n = gets.to_i) != -1
  arr = []
  n.times{ arr << gets.to_i }
  s = arr.reduce(:+)
  if s % n != 0
    puts(-1)
  else
    avg = s / n
    puts(arr.reduce(0){|r, x| r += x > avg ? x - avg : 0})
  end
end
