# man

## USAGE

- `man [man options] [[section] page ...] ...`
- `man -k [apropos options] regexp ...`
- `man -f [whatis options] page ...`

## OPTIONS

`-f, --whatis`

: Equivalent to whatis. Display a short description from the manual page, if available.

`-k, --apropos`

: Equivalent to apropos. Search the short manual page descriptions for keywords and display any matches.

## SECTIONS

| Section | Type                                                                                          |
| ------- | --------------------------------------------------------------------------------------------- |
| 1       | Executable programs or shell commands                                                         |
| 2       | System calls (functions provided by the kernel)                                               |
| 3       | Library calls (functions within program libraries)                                            |
| 4       | Special files (usually found in /dev)                                                         |
| 5       | File formats and conventions, e.g. /etc/passwd                                                |
| 6       | Games                                                                                         |
| 7       | Miscellaneous (including macro packages and conventions), e.g. man(7), groff(7), man-pages(7) |
| 8       | System administration commands (usually only for root)                                        |
| 9       | Kernel routines [Non standard]                                                                |

## EXAMPLES

1. `man ls` - display the manual page of **ls** command
2. `man -k ^man$` - search the short manual page descriptions for **man**
3. `man 7 man` - display the **man** page from section 7
4. `man -f ls` - display the short description from **ls** manual page
