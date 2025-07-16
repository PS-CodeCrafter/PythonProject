GIT COMMANDS

## Git Reset Hard
### Use got reset command to discard local changes and bring local to Head of origin/main
git reset --hard origin/main

## Git Stash
### Use git stash to stash local changes (staged changes) to apply later to branch. Include specific files to stash or 
### otherwise all files in staging area will be stashed
git stash push -- <path-to-file1> <path-to-file2>

### If there are untracked files to stash, use the below command
git stash push -u -- <path-to-file1> <path-to-file2>

### View the stash list
git stash list

### View the content of specific stash
git stash show stash@{0}
### View the content of stash (if there were untracked files included in stash)
git stash show -u stash@{0}
