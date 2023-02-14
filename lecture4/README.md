## Exercise4 - Data Wangling

Exercises for [lecture4](https://missing.csail.mit.edu/2020/data-wrangling/)

1. Take this short interactive [regex tutorial](https://regexone.com/).

2. 1. Find the number of words (in `/usr/share/dict/words`) that contain at least three `a`s and don’t have a `'s` ending.

```
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3,}.*$" | grep -v "\'s$" |wc -l
```

    - `tr "[:upper:] "[:lower:]"]` is used to make case insensitivity
    - `grep -v` is used to select the part of "not matching"

2. 2. What are the three most common last two letters of those words? `sed`’s `y` command, or the `tr` program, may help you with case insensitivity.

```
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3,}.*$" | grep -v "\'s$" | sed -E "s/.*([a-z]{2})$/\1/" | sort | uniq -c |sort -n |tail -n3
```

    - `sed -E "s/.*([a-z]{2}$/\1)/"` is used to substitute all found matches with the first capture group(the last two letters).

2. 3. How many of those two-letter combinations are there?

```
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3,}.*$" | grep -v "\'s$" | sed -E "s/.*([a-z]{2})$/\1/" | sort | uniq | wc -l
```

2. 4. And for a challenge: which combinations do not occur?

- output all last two letters to `last_letters`:

```
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3,}.*$" | grep -v "\'s$" | sed -E "s/.*([a-z]{2})$/\1/" > last_letters

```

- write a script to generate all possible combinations of last 2 letters in `all_letter.sh`:

```
#!/bin/bash

for i in {a..z}; do
  for j in {a..z}; do
    echo "$i$j" >> all_letters
  done
done
```

generate:
`source ./all_letters.sh`

- compare:

```
diff --changed-group-format='<' --unchanged-group-format='' all_letters last_letters
```

```
#for mac os
diff --changed-group-format='<' all_letters last_letters | grep '<'|sed -E 's/(.*<)//'
```

- The --changed-group-format option is set to %<, which tells diff to output only the lines from the first file that are not in the second file. The --unchanged-group-format option is set to an empty string, which tells diff to suppress output of lines that are the same in both files.
- for mac os, the GNU version of `diff` 's `--unchanged-group-format` isn't available, and the command will be `diff all_letters last_letters --changed-group-format='<' | grep '<'|sed -E 's/(.*<)//'`
- `--changed-group-format='<'` means using `<` to mark the content which appear in first file but does not appear in the second file.
- `grep '<'` and `sed -E 's/(.*<)//'` is used to remove the symbol and filter the result.

3. To do in-place substitution it is quite tempting to do something like `sed s/REGEX/SUBSTITUTION/ input.txt > input.txt`. However this is a bad idea, why? Is this particular to sed? Use man sed to find out how to accomplish this.

- This is a bad idea because the shell redirection operator `>` truncates the output file input.txt before sed starts processing the input file, which means that the original contents of input.txt will be lost before sed has a chance to read them. As a result, the output file will be empty or contain only the text produced by the sed command.

- To perform an in-place substitution with sed, you should use the `-i` flag followed by an optional backup extension, like `sed -i.bak 's/REGEX/SUBSTITUTION/' input.txt`, which will modify `input.txt` in place and create a backup copy with the specified extension.