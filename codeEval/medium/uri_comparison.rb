require 'uri'
File.open(ARGV[0]).each_line do |l|
  v = l.strip.split(';').collect! do |u|
    URI(URI.unescape(u)).normalize.to_s
  end.to_a.uniq.length
  puts ['False', 'True'][v%2]
end