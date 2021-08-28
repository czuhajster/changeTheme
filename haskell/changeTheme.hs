module Main where
    import AlacrittyConfig (changeLine)
    import System.IO
    import System.Directory
    import qualified Data.Yaml
    
    alacrittyConfigPath :: String
    alacrittyConfigPath = "alacritty_config.yml"

    main :: IO ()
    main = do readh <- openFile alacrittyConfigPath ReadMode
              -- Read config contents.
              configContents <- hGetContents readh
              -- Process config contents.
              let changedContents = processData configContents

              -- Get system's current temporary directory.
              tempDir <- getTemporaryDirectory
              -- Open temporary file
              (tempname, temph) <- openTempFile tempDir "foo.yml"
              -- Write line to the temporary file.
              hPutStr temph changedContents
              -- Close handles for input and temp files.
              hClose readh
              hClose temph
              -- Rename the temp file.
              renameFile tempname alacrittyConfigPath

    processData :: String -> String
    processData contents = unlines (changeLine (lines contents) "# normal:" "siusiak")
