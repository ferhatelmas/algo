while (n = gets.to_i) != 0
  arr = gets.chop.scan(/.{1,#{n}}/).each_with_index.map do |s, i|
    i%2 == 0 ? s.split(//) : s.split(//).reverse
  end
  arr = [[]] if arr.empty?
  arr[-1].fill('x', arr[-1].length..n-1)
  puts arr.transpose.each{|a| a.join('') }.join('')
end
