while gets.chomp != "0 0"
  b = gets.split.map{|n| n.to_i}
  c = gets.split.map{|n| n.to_i}.sort[1]
  puts b.any?{|n| n < c} ? "Y" : "N"
end
