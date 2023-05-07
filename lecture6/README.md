## Exercise 6 - Version Control(git)

Exercises for [lecture6](https://missing.csail.mit.edu/2020/version-control/)

1. If you don’t have any past experience with Git, either try reading the first couple chapters of [Pro Git](https://git-scm.com/book/en/v2) or go through a tutorial like [Learn Git Branching](https://learngitbranching.js.org/). As you’re working through it, relate Git commands to the data model.

2. Clone the repository for the class website.
- Explore the version history by visualizing it as a graph.

`git log --all --graph --decorate`

- Who was the last person to modify README.md? (Hint: use git log with an argument).

`git log -1 README.md `
```
commit 9ef9db72211fefc00caaa7133b35dda4a99acccf
Author: Anish Athalye <me@anishathalye.com>
Date:   Thu Oct 27 20:28:41 2022 -0400

    Add Docker setup for easier development
```   
- What was the commit message associated with the last modification to the collections: line of _config.yml? (Hint: use git blame and git show).

`git blame _config.yml`
```
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  1) # Setup
ac838248 (Anish Athalye 2023-02-19 20:01:43 -0500  2) title: 'Missing Semester'
d4412ead (Anish Athalye 2019-12-01 21:26:19 -0500  3) url: https://missing.csail.mit.edu
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  4)
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  5) # Settings
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  6) markdown: kramdown
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  7) kramdown:
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  8)   input: GFM
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  9)   hard_wrap: false
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 10) highlighter: rouge
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 11) permalink: /:title/
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 12) future: true
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 13) # safe: true # breaks local rendering if enabled
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 14) timezone: America/New_York
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 15) analytics:
1320c3c9 (Anish Athalye 2023-02-12 08:48:11 -0500 16)   tracking_id: G-P7WVHD84D1
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 17)
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 18) collections:
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 19)   '2019':
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 20)     output: true
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 21)   '2020':
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 22)     output: true
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 23)
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 24) # Excludes
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 25) exclude:
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 26)   - README.md
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 27)   - Gemfile
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 28)   - Gemfile.lock
fa309f93 (Anish Athalye 2020-05-16 11:13:27 -0400 29)   - vendor
```

`git show a88b4eac` 
```
Author: Anish Athalye <me@anishathalye.com>
Date:   Fri Jan 17 15:26:30 2020 -0500

    Redo lectures as a collection
```

3. One common mistake when learning Git is to commit large files that should not be managed by Git or adding sensitive information. Try adding a file to a repository, making some commits and then deleting that file from history (you may want to look at [this](https://help.github.com/articles/removing-sensitive-data-from-a-repository/)).

`git filter-repo --invert-paths --path PATH-TO-YOUR-FILE-WITH-SENSITIVE-DATA`

`git rm --cached --ignore-unmatch PATH-TO-YOUR-FILE-WITH-SENSITIVE-DATA --prune-empty --tag-name-filter cat -- --all`

4. Clone some repository from GitHub, and modify one of its existing files. What happens when you do git stash? What do you see when running `git log --all --oneline`? Run git stash pop to undo what you did with git stash. In what scenario might this be useful?

When you want to check other commits but still get some leftover on your current work which you don't want to make a commit.

5. Like many command line tools, Git provides a configuration file (or dotfile) called ~/.gitconfig. Create an alias in ~/.gitconfig so that when you run git graph, you get the output of `git log --all --graph --decorate --oneline`. Information about git aliases can be found [here](https://git-scm.com/docs/git-config#Documentation/git-config.txt-alias).

```
[alias]
graph = log --all --graph --decorate --oneline
```

6. You can define global ignore patterns in ~/.gitignore_global after running `git config --global core.excludesfile ~/.gitignore_global`. Do this, and set up your global gitignore file to ignore OS-specific or editor-specific temporary files, like .DS_Store.