module Simple where

import qualified Data.Yaml as Y

main :: IO ()
main = do
    res <- Y.decodeFileThrow "alacritty.yml"
    print res
