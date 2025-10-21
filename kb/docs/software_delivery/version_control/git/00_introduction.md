# Introduction

## What is Git?

Git is a distributed version control system that tracks changes by storing snapshots of the entire project state at each commit.

## Why use Git?

Instead of storing file differences (like traditional VCS), Git:

- Creates a snapshot of all files in the staging area.
- Stores each file as a Git object (called a blob) identified by a SHA-1 hash of its content.
- Uses trees to represent directory structures, and commits to point to those trees.
- Avoids duplication by reusing objects with identical content — if a file hasn’t changed, Git just references the existing blob.

So yes, Git stores everything in its object database using SHA-1 hashes, but it doesn’t hash the entire project as one — it hashes each object (file, tree, commit) individually.