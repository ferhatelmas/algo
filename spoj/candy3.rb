gets.to_i.times do |_|
  _, n = gets, gets.to_i
  s = (0...n).map{|_| gets.to_i}.inject(:+)
  puts(s % n == 0 ? 'YES' : 'NO')
end
