## Exercise5 - Command Line Environment

Exercises for [lecture5](https://missing.csail.mit.edu/2020/command-line/)

### Job Control

1. we can use some `ps aux | grep` commands to get our jobs’ pids and then kill them, but there are better ways to do it. Start a `sleep 10000` job in a terminal, background it with `Ctrl-Z` and continue its execution with `bg`. Now use `pgrep` to find its pid and `pkill` to kill it without ever typing the pid itself. (Hint: use the `-af` flags).

```
sleeep 10000
[1]  + 27949 suspended  sleep 10000
bg
[1]  + 27949 continued  sleep 10000
```

```
     -a                Include process ancestors in the match list.  By default, the current pgrep
                       or pkill process and all of its ancestors are excluded (unless -v is used).

     -f                Match against full argument lists.  The default is to match against process
                       names.
```

```
pgrep -af "sleep 10000" // print the pid
pkill -af "sleep 10000" // kill the process without typing pid
```

2. a. Say you don’t want to start a process until another completes. How would you go about it? In this exercise, our limiting process will always be `sleep 60 &`. One way to achieve this is to use the `wait` command. Try launching the sleep command and having an `ls` wait until the background process finishes.

```
sleep 60&
wait $!
ls
```

- `wait $!` waits for the background process to finish. The `$!` variable contains the process ID of the last background process launched, so this command waits for the sleep process to finish.

b. However, this strategy will fail if we start in a different bash session, since wait only works for child processes. One feature we did not discuss in the notes is that the `kill` command’s exit status will be zero on success and nonzero otherwise. `kill -0` does not send a signal but will give a nonzero exit status if the process does not exist. Write a bash function called pidwait that takes a pid and waits until the given process completes. You should use `sleep` to avoid wasting CPU unnecessarily.

```
pidwait(){
  while kill -0 $1 2>/dev/null; do
    sleep 1
  done
}
```
