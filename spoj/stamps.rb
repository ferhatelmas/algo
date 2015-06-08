gets.to_i.times do |t|
  n, i = gets.split.map{|e| e.to_i}
  arr = gets.split.map{|e| e.to_i}.sort.reverse

  s = c = 0
  while s < n and c < i
    s += arr[c]
    c += 1
  end
  puts "Scenario ##{t+1}:"
  puts s >= n ? c : "impossible"
  puts
end
