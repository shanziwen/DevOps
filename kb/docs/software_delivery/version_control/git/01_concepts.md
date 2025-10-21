# Concepts

## Four States
`untracked`
: The files in the working directory that were not in the last snapshot and are not in the staging area.

`modified`
: The file has been changed but not committed in to the database yet.

`staged`
: The file has been modified and marked in its current version to go into next commit snapshot.

`committed`
: The data is safely stored in the local database

## Three Main Sections
`Working Tree`
: A single checkout of one version of the project. There files are pulled out of the compressed database in the Git directory and placed on disk to use or modify

`Staging Area`
: A file that stores information about what will go into next commit. Also known as `index`

`Git Directory`
: A directory where Git stores the metadata and object database. It is what is copied when a repository is cloned from another computer

## Git Objects
There're four types of git object:

- blob: Git stores each file as a blob object.
- tree: Git stores directory as tree object.
- commit: Git store the metadata of commit as commit object.
- tag: Git store the metadata of annotated tag as tag object.

### How Git Store Files?
Git stores each file as a blob object. To create this object, Git: 

1. constructs a headered string. It prepends the file content with a header in the format:
    ``` 
    blob <content_byte_size>\0<file_content>
    ```
    - `<content_byte_size>` is the size of the file in bytes.
    - `\0` is a null byte separator.
2. computes the SHA-1 hash of this entire string (header + content). This produces a 40-character hexadecimal hash, which becomes the object ID.
3. compresses the string using zlib and stores it as a file under `.git/objects/`. The storage path is split:
    - The first two characters of the hash form the directory name.
    - The remaining 38 characters form the filename inside that directory.
    - For example, if the hash is e69de29bb2d1d6434b8b29ae775ad8c2e48c5391, the blob is stored as: .git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391

## Git Directory Structure
|item|Usage|
|----|----|
|hooks/|Contains client-side or server-side scripts triggered by Git actions (e.g., pre-commit, post-merge).|
|info/|Stores auxiliary data like the global exclude file (exclude) for ignored patterns.|
|objects/|Stores all Git objects (blobs, trees, commits, tags) compressed and named by SHA-1 hash.|
|refs/heads/|Contains pointers to local branches (e.g., main, feature-x). Each file holds the latest commit hash.|
|refs/tags/|Stores tag references, which point to specific commits or objects for versioning.|
|refs/remotes/|Tracks remote branches (e.g., origin/main) for synchronization and fetch/pull operations.|
|description|Used by GitWeb to describe the repository. Ignored by Git itself in most workflows.|
|config|Repository-specific configuration file (e.g., remotes, user info, settings). Overrides global config.|
|HEAD|Points to the current branch or commit checked out. Can be symbolic (e.g., ref: refs/heads/main) or detached.|
|index|Staging area (also called cache). Tracks what’s staged for the next commit. Binary format.|

## Refspecs & References
`HEAD`
: A special reference that points to your current position in the repository — usually the latest commit on the branch you have checked out.

`refs`
: A human-readable name that points to a specific Git object — usually a commit. It acts like a symbolic label for navigating the Git history.

`remotes`
: A reference to another version of your repository — typically hosted on a server like GitHub, GitLab, or Bitbucket. It allows you to collaborate, synchronize, and share changes between your local repo and others.

## Fast-forward
A fast-forward occurs when the branch you're merging into has no new commits since the branch you're merging from. Git can simply moves the pointer forward — no merge commit is needed. You can also specify to create a merge commit explicitly by passing `--no-ff` option to `git merge` command, or disable fast-forward globally by running `git config --global merge.ff false`  

## Detached HEAD
A detached HEAD state happens when HEAD points directly to a commit instead of a branch.