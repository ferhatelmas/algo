gets.to_i.times do |_|
  n = gets.to_i
  puts n % 2 == 0 ? n.to_s(2).reverse.to_i(2) : n
end
