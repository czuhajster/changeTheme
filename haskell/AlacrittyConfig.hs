module AlacrittyConfig where
    changeLine :: [String] -> String -> String -> [String]
    changeLine [] _ _ = []
    changeLine (l:ls) x y = if l == x then
                                      y : changeLine ls x y
                            else 
                                      l : changeLine ls x y

