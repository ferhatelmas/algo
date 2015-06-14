while (a = gets)
  h = Hash.new 0
  a.chomp.split('').each{|e| h[e] += 1}
  puts gets.chomp.split('').select{|e| h[e] > 0 ? (h[e] -= 1; true) : false}.sort.join('')
end
