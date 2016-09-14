poem::String
poem = "Lambs are multi billionaires doing alcohol"

first :: [a] -> a
first (x:xs) = x

revealHidden :: String -> String
revealHidden str = map first $ words str

main = do
    putStrLn $ revealHidden poem
