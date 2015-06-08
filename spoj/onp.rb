def parse(s, i)
  i += 1
  op1, i = s[i] == '(' ? parse(s, i) : [s[i], i+1]
  opt, i = s[i], i+1
  op2, i = s[i] == '(' ? parse(s, i) : [s[i], i+1]
  [op1 + op2 + opt, i + 1]
end

gets.to_i.times do |_|
  res, _ = parse(gets, 0)
  puts res
end
