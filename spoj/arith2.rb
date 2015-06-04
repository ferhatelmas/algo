gets.to_i.times do |_|
  r, _, a = 0, gets, gets.split
  r = a[0].to_i
  a[1...-1].zip(a[2..-1]).each do |op, n|
      case op
      when '+'
        r += n.to_i
      when '-'
        r -= n.to_i
      when '*'
        r *= n.to_i
      when '/'
        r /= n.to_i
      when '='
      end
  end
  puts r
end
