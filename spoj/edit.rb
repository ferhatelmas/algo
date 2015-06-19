def diff(s)
  u, ui, li = true, 0, 0
  s.split('').each do |e|
    if (e.upcase == e) == u
      li += 1
    else
      ui += 1
    end
    u = !u
  end
  [ui, li].min
end

while (s = gets)
  puts diff(s.chomp)
end
