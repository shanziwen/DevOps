# Advanced
## Cherry Pick
- git cherry-pick

## Sub Module
- git submodule

## Plumbing Commands
- git rev-parse

- git bisect

## Ancestry Reference
  - ^N the Nth parent
  - ~N the first parent (of first parent of .. N)
## Commit Range
  - A..B (Reachable from B but not A)
  - A...B (Reachable from A or B but not both)
  - A B .. --not C | ^C (Reachable from any of A, B ... but not C)
## Commit Template: `git config commit.template <path>`
## Refspec
  - Syntax: `[+]<src>:<dst>`
  - `+` - optional, Update the reference even if it isn't a fast-forward
  - `<src>` - the pattern for references on the remote side
  - `<dst>` - where remote reference will be tracked locally
  - Example: `+refs/heads/*:refs/remotes/origin/*`