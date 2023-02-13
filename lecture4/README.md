## Exercise4 - Data Wangling

Exercises for [lecture4](https://missing.csail.mit.edu/2020/data-wrangling/)

1. Take this short interactive [regex tutorial](https://regexone.com/).

2.

- Find the number of words (in `/usr/share/dict/words`) that contain at least three `a`s and don’t have a `'s` ending.

```
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3,}.*$" | grep -v "\'s$" |wc -l
```

- `tr "[:upper:] "[:lower:]"]` is used to make case insensitivity
- `grep -v` is used to select the part of "not matching"
- What are the three most common last two letters of those words? `sed`’s `y` command, or the `tr` program, may help you with case insensitivity.

```
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3,}.*$" | grep -v "\'s$" | sed -E "s/.*([a-z]{2})$/\1/" | sort | uniq -c |sort -n |tail -n3
```

-
- How many of those two-letter combinations are there? And for a challenge: which combinations do not occur?
