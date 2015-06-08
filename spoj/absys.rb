gets.to_i.times do |_|
  _, s = gets, gets.split
  if s[0].include?('machula')
    puts "#{s[4].to_i-s[2].to_i} + #{s[2]} = #{s[4]}"
  elsif s[2].include?('machula')
    puts "#{s[0]} + #{s[4].to_i-s[0].to_i} = #{s[4]}"
  else
    puts "#{s[0]} + #{s[2]} = #{s[0].to_i+s[2].to_i}"
  end
end
