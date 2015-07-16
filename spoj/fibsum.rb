P = 5 ** 0.5
def g(n)
  puts n
  ((P + 1) ** n - (1 - P)) / (P * 2 ** n)
end

gets.to_i.times do |_|
  n = gets.to_i
  puts "%0.f" % (g(n + 11) - g(n + 1) + g(n + 6) % 10)
end
