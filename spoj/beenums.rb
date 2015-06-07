while (n = gets.to_i) != -1
  if n == 1
    puts 'Y'
  else
    n, i = n-1, 1
    while n > 0
      n -= 6 * i
      i += 1
    end
    puts n == 0 ? 'Y' : 'N'
  end
end
