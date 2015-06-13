gets.to_i.times do |_|
  a, b, c, d = gets.split.map{|f| f.to_f}
  s = (a + b + c + d) / 2
  puts("%.2f" % ((s-a) * (s-b) * (s-c) * (s-d))**0.5)
end
