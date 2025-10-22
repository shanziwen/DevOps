# Advanced
## Cherry Pick
- `git cherry-pick` - Apply the changes introduced by some existing commits

## Plumbing Commands
- `git rev-parse`
- `git rev-list` - Lists commit objects in reverse chronological order

## Ancestry Reference
  - ^N the Nth parent
  - ~N the first parent (of first parent of .. N)

## Revision Range
  - A..B (Reachable from B but not A)
  - A...B (Reachable from A or B but not both)
  - A B .. --not C | ^C (Reachable from any of A, B ... but not C)

## Refspec
  - Syntax: `[+]<src>:<dst>`
  - `+` - optional, Update the reference even if it isn't a fast-forward
  - `<src>` - the pattern for references on the remote side
  - `<dst>` - where remote reference will be tracked locally
  - Example: `+refs/heads/*:refs/remotes/origin/*`