-- 1A
main = do
  ln <- getLine
  let ls = map read (words ln)
  putStrLn $ show $ fillTiles (ls !! 0) (ls !! 1) (ls !! 2)

fillTiles :: Double -> Double -> Double -> Integer
fillTiles m n k = (ceiling $ m / k) * (ceiling $ n / k)