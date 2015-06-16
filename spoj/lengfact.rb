gets.to_i.times do |_|
  n = gets.to_i
  if n < 3
    puts 1
  else
    puts(((n*Math.log(n) - n + (Math.log 2*n*Math::PI) / 2) / Math.log(10)).floor + 1)
  end
end
