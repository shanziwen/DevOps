# Package Manager
## APT

### Remove downloaded package files
sudo apt clean

### Remove outdated package files (safer than full clean)
sudo apt autoclean

### Remove unused dependencies
sudo apt autoremove

## DNF/YUM
### Remove cached packages and metadata
sudo yum clean all

### Optional: Remove unused packages and dependencies
sudo package-cleanup --leaves
sudo package-cleanup --orphans