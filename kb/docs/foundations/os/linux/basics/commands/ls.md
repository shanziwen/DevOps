# ls

*list directory contents*

## SYNOPSIS

`ls [OPTION]... [FILE]...`

## OPTIONS

`-d, --directory`

: list directories themselves, not their contents

`-h, --human-readable`
: with -l and -s, print sizes like 1K 234M 2G etc.

`--sort=WORD`
: sort by WORD instead of name: none (-U), size (-S), time (-t), version (-v), extension (-X)

`-l`
: use a long listing format

`-t`
: sort by time, newest first;

`-c`
: with `-lt`: sort by, and show, ctime (time of last modification of file status information); with `-l`: show  ctime andsort by name; otherwise: sort by ctime, newest first

`--time=WORD`
: change the default of using modification times; access time (`-u`): atime, access, use; change time (`-c`): ctime, status; birth time: birth, creation; with `-l`, WORD determines which time to show; with `--sort=time`, sort by WORD (newest first)

`-a, --all`

: do not ignore entries starting with .

`-i, --inode`
: print the index number of each file

`-I, --ignore=PATTERN`
: do not list implied entries matching shell PATTERN

## EXAMPLES

1. Display the content of `~/.ssh` directory and sort by time (newest first)
    ```
    vagrant@ubuntu2204:/vagrant/kb$ ls -lat ~/.ssh
    total 28
    drwxr-x--- 10 vagrant vagrant 4096 Mar 22 08:24 ..
    drwx------  2 vagrant vagrant 4096 Mar  2 07:38 .
    -rw-------  1 vagrant vagrant  978 Mar  2 07:38 known_hosts
    -rw-rw-r--  1 vagrant vagrant   88 Mar  2 07:37 config
    -rw-------  1 vagrant vagrant  388 Mar  2 07:37 github.pem
    -rw-r--r--  1 vagrant vagrant  142 Mar  2 07:28 known_hosts.old
    -rw-------  1 vagrant vagrant  409 Jan  6  2024 authorized_keys
    ```

2. Display the content of `~/.ssh` directory and ignore files starting with *know*
    ```
    vagrant@ubuntu2204:/vagrant/kb$ ls -lat -I know* ~/.ssh
    total 20
    drwxr-x--- 10 vagrant vagrant 4096 Mar 22 08:24 ..
    drwx------  2 vagrant vagrant 4096 Mar  2 07:38 .
    -rw-rw-r--  1 vagrant vagrant   88 Mar  2 07:37 config
    -rw-------  1 vagrant vagrant  388 Mar  2 07:37 github.pem
    -rw-------  1 vagrant vagrant  409 Jan  6  2024 authorized_keys
    ```