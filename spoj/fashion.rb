def arr
  gets.split.map{|s| s.to_i}.sort!
end

gets.to_i.times do |_|
  gets
  puts(arr.zip(arr).reduce(0){|s, n| s + n[0] * n[1]})
end
