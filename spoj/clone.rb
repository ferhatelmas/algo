while (s = gets.chomp) != "0 0"
  n, m = s.split.map{|e| e.to_i}
  h = Hash.new(0)
  n.times{|_| h[gets.chomp] += 1}
  res = Array.new(n, 0)
  h.each{|_, v| res[v-1] += 1}
  res.each{|v| puts v}
end
