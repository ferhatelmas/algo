while (k = gets.to_f) != 0
  s, i = 0, 1
  while s <= k
    s += 1.0 / (i+1)
    i += 1
  end
  puts("#{i-1} card(s)")
end
