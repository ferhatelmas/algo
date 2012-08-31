n = STDIN.gets.to_i
1.upto(n)  do 
  a, b = STDIN.gets.split(' ')
  puts (a.reverse.to_i + b.reverse.to_i).to_s.reverse.to_i
end