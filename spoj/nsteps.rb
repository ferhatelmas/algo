i, n = 0, gets.to_i
while i < n
  a, b = gets.split.map{|x| x.to_i}
  if a == b
    puts a % 2 == 0 ? a * 2 : a * 2 - 1
  elsif a == b + 2
    puts a % 2 == 0 ? a * 2 - 2 : a * 2 - 3
  else
   puts 'No Number'
  end
  i += 1
end
