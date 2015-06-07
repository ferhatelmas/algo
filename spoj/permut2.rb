while gets.to_i > 0
  arr = gets.split.map{|n| n.to_i}
  res = arr.each_with_index.find{|n, i| arr[n-1] != i+1}
  puts((res ? "not ambiguous" : "ambiguous"))
end
