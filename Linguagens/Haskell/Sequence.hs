import Data.List

main :: IO ()
main = do

  let f :: Int -> [Int]
      f a = [1..a]
  
  let g :: Int -> [Int]
      g b = [2..b] ++ collatzSequence b

  let prime = sieve [2..] where
      sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0]

  print $ f 4
  print $ drop 6 $ g 7
  print $ take 4 prime

collatzSequence :: Int -> [Int]
collatzSequence n
  | n == 1    = [1]
  | even n    = n : collatzSequence (n `div` 2)
  | otherwise = n : collatzSequence (n * 3 + 1)