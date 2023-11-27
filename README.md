TidyUpDirectory
=============================
This is a simple python application which is used to tidy up any given directory.
It segregates the files in a directory into PDF, TEXT and IMAGES folders.

What it does?
=============================
Provide the target directory (absolute path) which needs to be tidy up as a command line argument
This application then creates directories under the target directory
1. /Pdf -> for all the PDF (.pdf) files
2. /Text -> for all the text (.txt) files
3. /Images - > for all the image (.png, .jpg) files

And then moves the files under the target directory to these respective directories.
If the file does not belong to any of the above types, it is skipped (which means it remains in the target directory)

How to use
=============================
1. Clone the repo
2. Use pyinstaller and create a executable.
   For example, I have an executable `main` under the `/dist` directory. Copy this file to any location on your system, rename it to `TidyUpDirecotry`. Create a shell script in the same location, say `runTidyUpdirectory.sh` copy the following lines and save it.
   ```
   #!/bin/bash

   ./TidyUpDirectory
   ```
   
4. Now we can run the shell script file.
5. By default the program considers `/Downloads` directory (MacOS). In case you want run it on a different directory replace 2nd line in the shell script to following
   ```
   ./TidyUpDirectory <absolute/path/to/desired/direcotry>
   ```
   