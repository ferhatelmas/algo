while (s = gets)
  a, b, c, m, n = s = s.split.map{|e| e.to_i}
  break if s.uniq.length == 1 and s[0] == 0
  dx, dy = m * a, n * b
  ang = Math.atan2(dy, dx) * 180 / Math::PI
  v = (dx**2 + dy**2)**0.5 / c
  puts "%.2f %.2f" % [ang, v]
end
