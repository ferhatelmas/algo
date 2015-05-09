gets.to_i.times do
  puts gets.split.chunk{ |s| s.length }.to_a.map{ |arr| arr[1].length }.max
end
