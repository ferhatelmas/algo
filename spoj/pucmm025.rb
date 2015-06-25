while (s = gets.chomp)
  h, c, n = Hash.new, 0, s.to_i
  s.split("").each do |e|
    if e != "0"
      h[e] = n % e.to_i == 0 unless h.include? e
      c += h[e] ? 1 : 0
    end
  end
  puts c
end
