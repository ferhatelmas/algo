while (l = gets.split.map{|x| x.to_i}.uniq) != [0]
   puts l[2] - l[1] == l[1] - l[0] ? "AP #{l[2] * 2 - l[1]}" : "GP #{l[2]**2 / l[1]}"
end
