def k(ss)
  ss.split(' ').map{|s| s.to_i}.max
end

gets.to_i.times do |_|
  _, _, g, m = gets, gets, k(gets), k(gets)
  puts g >= m ? 'Godzilla' : 'MechaGodzilla'
end
