## Exercise1- Course overview + the shell

Exercises for [lecture 1](https://missing.csail.mit.edu/2020/course-shell/)
1. Create a new director called `missing` under `/tmp`.

```
touch /tmp/missing
```

2. Use touch to create a new file called semester in missing.

```
touch semester /tmp/missing
```

3. Write the following into that file, one line at a time:
```
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```
- Bash treats single-quoted strings (') differently: they will do the trick in this case. See the Bash [quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html) manual page for more information.
```
echo '#!/bin/sh' >> /tmp/mission/semester
echo 'curl --head --silent https://missing.csail.mit.edu' >> /tmp/missing/semester
```


4. Try to execute the file, i.e. type the path to the script (./semester) into your shell and press enter. Understand why it doesn’t work by consulting the output of ls (hint: look at the permission bits of the file).

```
ls -l |grep semester                                                                                    
15:-rw-r--r--   1 mottapippi  staff    10 Feb  2 11:00 semester
```
- `-rw` shows the permission of `mottapippi`, which includes `read` and `write`, but without `execute`.

5. Run the command by explicitly starting the `sh` interpreter, and giving it the file `semester` as the first argument, i.e. `sh semester`. Why does this work, while `./semester` didn’t?

- By using `man sh`, we can know that `sh` is `a POSIX-compliant command interpreter (shell)`, which is interpreting the file `semester`.

6. Look up the chmod program (e.g. use man chmod).
- `chmod` is used to change file modes or Access Control Lists.

7. Use chmod to make it possible to run the command ./semester rather than having to type sh semester.
```
chmod a+x semester
```
- add `execution` permission to user, group and everyone else.

8. Use | and > to write the “last modified” date output by semester into a file called `last-modified.txt` in your home directory.

```
date -r ./semester | cat ~/last-modified.txt
```


