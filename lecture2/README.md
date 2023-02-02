## Exercise2- Shell Tools and Scripting

Exercises for [lecture 2](https://missing.csail.mit.edu/2020/shell-tools/)

1. Read `man ls` and write an ls command that lists files in the following manner

- Includes all files, including hidden files
- Sizes are listed in human readable format (e.g. 454M instead of 454279954)
- Files are ordered by recency
- Output is colorized

A sample output would look like this
```
 -rw-r--r--   1 user group 1.1M Jan 14 09:53 baz
 drwxr-xr-x   5 user group  160 Jan 14 09:53 .
 -rw-r--r--   1 user group  514 Jan 14 06:42 bar
 -rw-r--r--   1 user group 106M Jan 13 12:12 foo
 drwx------+ 47 user group 1.5K Jan 12 18:08 ..
```
Using macOS:
```
ls -alhtG
```

2. Write bash functions `marco` and `polo` that do the following. Whenever you execute `marco` the current working directory should be saved in some manner, then when you execute `polo`, no matter what directory you are in, `polo` should `cd` you back to the directory where you executed `marco`. For ease of debugging you can write the code in a file `marco.sh` and (re)load the definitions to your shell by executing `source marco.sh`.

```
#!/bin/bash
marco() {
    export MARCO_PATH=$(PWD)
}

polo(){
    cd "$MARCO_PATH"
}
```

3. Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run. Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end. Bonus points if you can also report how many runs it took for the script to fail.

```
# random.sh
 #!/usr/bin/env bash

 n=$(( RANDOM % 100 ))

 if [[ n -eq 42 ]]; then
    echo "Something went wrong"
    >&2 echo "The error was using magic numbers"
    exit 1
 fi

 echo "Everything went according to plan"
```
```
#debug.sh
#!/bin/bash
count=0
until [ "$?" -ne 0 ];
do
  count=$((count+1))
  ./random.sh &> out.txt
done

echo "Repeat: it took $((count)) times for the script to fail"
```

4. As we covered in the lecture `find`’s `-exec` can be very powerful for performing operations over the files we are searching for. However, what if we want to do something with all the files, like creating a zip file? As you have seen so far commands will take input from both arguments and STDIN. When piping commands, we are connecting STDOUT to STDIN, but some commands like tar take inputs from arguments. To bridge this disconnect there’s the `xargs` command which will execute a command using STDIN as arguments. For example `ls | xargs` rm will delete the files in the current directory.

Write a command that recursively finds all HTML files in the folder and makes a zip with them. Note that your command should work even if the files have spaces (hint: check -d flag for xargs).

```
# Using macOS
find . -type f -name "*.html" -print0| xargs -0 tar -d zcvf html.tar.gz
```
- If you’re on macOS, note that the default BSD find is different from the one included in GNU coreutils. You can use -print0 on find and the -0 flag on xargs. 
- The `-print0` option in a macOS shell command is used with the find command to print the results, separating filenames with the null character (\0) instead of the newline character (\n).
- The `-0 option` in xargs is used to specify that the input will be separated by null characters (\0) instead of whitespace characters (space, tab, newline, etc.). This is useful when dealing with filenames that contain whitespace characters, which can cause issues when passed as arguments to other commands.

5. (Advanced) Write a command or script to recursively find the most recently modified file in a directory. More generally, can you list all files by recency?
```
# list all files by recency
ls -alt

# recursively find the most recentlt modified file in a directory
find ./path/to/find -type f -print0 | xargs -0 stat -f "%m %N" | sort -nr | head -1

# return
1675333967 ./Desktop/lernen/mit-missing-semester/lecture2/README.md
```
- `xargs -0 stat -f "%m %N"`: This command uses xargs with the `-0` option to read the filenames separated by null characters, and passes them as arguments to the stat command. The stat command is used to retrieve file information, and the `-f` option is used to specify a format for the output, in this case `"%m %N"`, which will output the modification time (%m) and the file name (%N), separated by a space.
- `sort -nr`: This command sorts the output of the previous command in reverse order `(-r)` by the modification time, `(-n)` is used to sort the input numerically (timestamps).
- To remove `167533967`, you can use one more pipeline `cut -d' ' -f2-` to just leave the name of file.The `-d` option specifies the delimiter used to separate fields (space). The `-f2-` option in the cut command specifies the fields to be extracted from the input(from the second field to the end of the line).