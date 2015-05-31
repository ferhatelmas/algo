puts((1..gets.to_i).reduce(0) do |n, i|
  n + (1..i**0.5).reduce(0){|t, j| t + (i % j == 0 ? 1 : 0)}
end)
