puts readlines("\n")[1..-1].reduce(0){|n, s| n ^ s.to_i}
