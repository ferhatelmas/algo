while (s = gets)
  s, b1, b2 = s.split
  s = s.to_i(b1.to_i).to_s(b2.to_i)
  puts s.length > 7 ? 'ERROR' : s.upcase.rjust(7, ' ')
end
