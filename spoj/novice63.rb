def comb(n, r)
  r = n - r if r > n / 2
  res = 1
  (0...r).each{|i| res = (res * (n - i)) / (i + 1)}
  res
end

dp = [1, 1, 1]
(3...60).each do |i|
  if i % 2 == 0
    dp << dp[i-1]
  else
    dp << dp[i-1] + comb(i, (i+1) / 2)
  end
end

gets.to_i.times do |_|
  puts dp[Math.log2(gets.to_i).to_i-1]
end
