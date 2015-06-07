gets.to_i.times do |_|
  n, k = gets.split.map{|s| s.to_i}
  a = gets.split.map{|s| s.to_i}.sort
  puts((1..n-k).inject(a[k-1] - a[0]){|r, i| [r, a[i+k-1] - a[i]].min})
end
