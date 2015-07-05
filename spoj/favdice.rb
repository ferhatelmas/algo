gets.to_i.times do |_|
  n, res = gets.to_f, 0.0
  (1..n).each{|i| res += n / i}
  puts "%.2f" % res
end
