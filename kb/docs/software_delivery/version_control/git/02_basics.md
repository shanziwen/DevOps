# Basics
## Installation
Refer to [Install Git](https://git-scm.com/install/windows)
## Setup & Configuration
- `git config` - Get and set repository or global options

    **Configuration Level**
    
    |Scope|Configuration Path|CLI Options|
    |----|----|----|
    |System Level|`/etc/gitconfig`|`--system`|
    |Global(User) Level|`~/.gitconfig`, `~/.config/git/config`|`--global`|
    |Local Level|`.git/config`|`--local`|

    **Common Configuration**
    
    |name|usage|
    |----|----|
    |user.name|the name used in author and committer field of commit objects|
    |user.email|the email used in author and committer field of commit objects|
    |user.signingKey|the key used to sign the commit/tag objects|
    |merge.ff|if create a fast-forward merge when possible|
    |pull.rebase|if rebased branches on top of the fetch branch, instead of merging|
    |init.defaultBranch|the default branch when initialize a new repository|
    |commit.template|specify the pathname of a file to use as the template for new commit messagesq|


- `git init` - Create an empty Git repository or reinitialize an existing one
- `git clone` - Clone a repository into a new directory

## Staging/Committing
- `git add` - Add file contents to the index
- `git commit` - Record changes to the repository
- `git status` - Show the working tree status
- `git diff` - Show changes between commits, commit and working tree, etc

## Branching & Merging
- `git branch` - List, create, or delete branches
- `git checkout` - Switch branches or restore working tree files
- `git switch` - Switch branches
- `git merge` - Join two or more development histories together
- `git rebase` - Reapply commits on top of another base tip

## Remote Work
- `git remote` - Manage set of tracked repositories
- `git fetch` - Download objects and refs from another repository
- `git pull` - Fetch from and integrate with another repository or a local branch
- `git push` - Update remote refs along with associated objects

## History & Logs
- `git log` - Show commit logs
- `git show` - Show various types of objects
  
## Undo & Recovery
- `git reset` - Reset current HEAD to the specified state
- `git revert` - Revert some existing commits
- `git restore` - Restore working tree files
- `git clean` - Remove untracked files from the working tree

## Remove
- `git rm` - Remove files from the working tree and from the index

## Rename  
- `git mv` - Move or rename a file, a directory, or a symlink

## Tagging
- `git tag` - Create, list, delete or verify a tag object signed with GPG

## Stash
- `git stash` - Stash the changes in a dirty working directory away
 
# Exclude Files(`.gitignore` file)
  - \# for command
  - glob pattern
  - start with / to avoid recursivity
  - end with / to specify directory
  - \! for negate a pattern 